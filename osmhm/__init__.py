import fetch
import filters


def run():
    """
    """
    import osmhm
    import osmdt
    import datetime
    import time

    while True:

        sequence = osmhm.fetch.fetch_last_read()

        if not sequence:
            osmhm.fetch.fetch_next(reset=True)
            sequence = osmhm.fetch.fetch_last_read()

        if sequence['read_flag'] == False:
            print "Processing sequence %s." % (sequence['sequencenumber'])

            data_stream = osmdt.fetch(sequence['sequencenumber'])
            data_object = osmdt.process(data_stream)

            changesets = osmdt.extract_changesets(data_object)
            objects = osmdt.extract_objects(data_object)
            users = osmdt.extract_users(data_object)

            osmhm.filters.suspiciousFilter(changesets)
            osmhm.filters.objectFilter(objects)
            osmhm.filters.userFilter(changesets)

        if sequence['timetype'] == 'minute':
            delta_time = 1
            extra_time = 10
        elif sequence['timetype'] == 'hour':
            delta_time = 60
            extra_time = 60
        elif sequence['timetype'] == 'day':
            delta_time = 1440
            extra_time = 300

        next_time = datetime.datetime.strptime(sequence['timestamp'], 
                        "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(minutes=delta_time)

        if datetime.datetime.utcnow() < next_time:
            sleep_time = (next_time - datetime.datetime.utcnow()).seconds + delta_time # We add an order of time smaller pause
            print "Waiting %2.1f seconds for the next file." % (sleep_time)
        else:
            sleep_time = 0

        time.sleep(sleep_time)

        count = 0
        while True:
            try:
                count += 1
                osmhm.fetch.fetch_next(sequence['sequencenumber'])
                break
            except:
                if count == 5: raise Exception('New state file not retrievable after five times.')
                print "Waiting %2.1f more seconds..." % (extra_time)
                time.sleep(extra_time)
