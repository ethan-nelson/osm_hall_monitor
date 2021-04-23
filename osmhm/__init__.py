from osmhm import (
    fetch,
    filters,
    inserts,
    tables,
    config,
    send_notification,
)


def run(time_type='hour', history=False, suspicious=False, monitor=True,
        notification=False, notifier=send_notification.basic_send_mail):
    """
    """
    import osmhm
    import osmdt
    import datetime
    import time

    while True:
        sequence = osmhm.db.get_last_file()

        if not sequence:
            osmhm.fetch.fetch_next(time_type=time_type, reset=True)
            sequence = osmhm.db.get_last_file()

        if sequence['read'] is False:
            print("Processing sequence %s." % (sequence['sequence']))

            count = 0
            while True:
                try:
                    count += 1
                    data_stream = osmdt.fetch(sequence['sequence'], time=time_type)
                    break
                except:
                    if count == 5:
                        msg = 'Current state file not retrievable after five times.'
                        raise Exception(msg)
                    print("File not reachable; waiting 60 more seconds...")
                    time.sleep(60)

            data_object = osmdt.process(data_stream)
            del data_stream

            changesets = osmdt.extract_changesets(data_object)
            objects = osmdt.extract_objects(data_object)
            users = osmdt.extract_users(data_object)
            del data_object

            if history:
                osmhm.inserts.insert_all_changesets(changesets)

            if suspicious:
                osmhm.filters.suspicious_filter(changesets)

            if monitor:
                osmhm.filters.object_filter(objects, notification=notification, notifier=notifier)
                osmhm.filters.user_filter(changesets, notification=notification, notifier=notifier)
                #osmhm.filters.user_object_filter(objects, notification=notification, notifier=notifier)  # not implemented yet
                osmhm.filters.key_filter(objects, notification=notification, notifier=notifier)

            del changesets, objects, users

            osmhm.db.update_last_file(sequence['sequence'], sequence['timestamp'], sequence['timetype'], True)
            print("Finished processing %s." % (sequence['sequence']))

        if sequence['timetype'] == 'minute':
            delta_time = 1
            extra_time = 10
        elif sequence['timetype'] == 'hour':
            delta_time = 60
            extra_time = 120
        elif sequence['timetype'] == 'day':
            delta_time = 1440
            extra_time = 300

        next_time = datetime.datetime.strptime(sequence['timestamp'],
                      "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(minutes=delta_time)

        if datetime.datetime.utcnow() < next_time:
            sleep_time = (next_time - datetime.datetime.utcnow()).seconds + delta_time
            print("Waiting %2.1f seconds for the next file." % (sleep_time))
        else:
            sleep_time = 1

        time.sleep(sleep_time)

        count = 0
        while True:
            try:
                count += 1
                osmhm.fetch.fetch_next(sequence['sequence'], time_type=time_type)
                break
            except:
                if count == 5:
                    msg = 'New state file not retrievable after five times.'
                    raise Exception(msg)
                print("Waiting %2.1f more seconds..." % (extra_time))
                time.sleep(extra_time)
