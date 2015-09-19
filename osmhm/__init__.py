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
            omshm.filters.objectFilter(objects)
            osmhm.filters.userFilter(users)

        if sequence['timetype'] == 'minute':
            delta_time = 1
        elif sequence['timetype'] == 'hour':
            delta_time = 60
        elif sequence['timetype'] == 'day':
            delta_time = 60*24

        next_time = datetime.datetime.strptime(sequence['timestamp'], 
                        "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(minutes=delta_time)

        if datetime.datetime.utcnow() < next_time:
            sleep_time = (next_time - datetime.datetime.utcnow()).seconds + delta_time * 60
            print "Waiting %2.1f seconds for the next file." % (sleep_time)
        else:
            sleep_time = 0

        time.sleep(sleep_time)

        osmhm.fetch.fetch_next(sequence['sequencenumber'])
