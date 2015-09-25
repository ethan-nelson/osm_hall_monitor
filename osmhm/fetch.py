from connect import connect
import requests
headers = {'user-agent': 'OSM Hall Monitor v0.3'}


def fetch_last_read():
    """
    """
    conn = connect()
    cur = conn.cursor()

    sequence = {}
    cur.execute("SELECT * FROM file_list;")
    try:
        foo, sequence['sequencenumber'], sequence['timestamp'],\
            sequence['timetype'], sequence['read_flag'] = cur.fetchone()

        return sequence
    except:
        return None


def fetch_next(current_sequence='', time_type='hour', reset=False):
    """
    """
    if reset is True:
        state_url = "http://planet.openstreetmap.org/replication/%s/state.txt" %\
            (time_type)

    else:
        next_sequence = int(current_sequence) + 1
        sequence_string = str(next_sequence).zfill(9)
        state_url = "http://planet.openstreetmap.org/replication/%s/%s/%s/%s.state.txt" %\
            (time_type, sequence_string[0:3], sequence_string[3:6], sequence_string[6:9])

    if time_type == 'minute':
        end = 5
    else:
        end = 3

    u = requests.get(state_url, headers=headers)

    if u.status_code == 404:
        raise Exception

    vals = u.text.encode('utf-8').split('\n')
    state = {}
    for val in vals[1:end]:
        (k, v) = val.split('=')
        state[k.lower()] = v.strip().replace("\\:", ":")

    info = (state['sequencenumber'], state['timestamp'], time_type, False)
    conn = connect()
    cur = conn.cursor()
    if reset is True:
        cur.execute("DELETE FROM file_list;")
        cur.execute("""INSERT INTO file_list
                       (sequence, timestamp, timetype, read)
                       VALUES (%s, %s, %s, %s);""", info)
    else:
        cur.execute("""UPDATE file_list SET
                       (sequence, timestamp, timetype, read)
                       = (%s, %s, %s, %s);""", info)
    conn.commit()
