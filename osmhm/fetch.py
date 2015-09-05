from connect import connect
import requests


def fetch_last_read():
    """
    """
    conn = connect()
    cur = conn.cursor()

    sequence = {}
    cur.execute("SELECT * FROM file_list;")
    foo, sequence['sequencenumber'], sequence['timestamp'], sequence['timetype'],\
        readflag = cur.fetchone()

    return sequence, readflag


def fetch_next(current_sequence='', time='hour', reset=False):
    """
    """
    if reset == True:
        state_url = "http://planet.openstreetmap.org/replication/%s/state.txt" %\
            (time)

    else:
        next_sequence = int(current_sequence) + 1
        sqnStr = str(next_sequence).zfill(9)
        state_url = "http://planet.openstreetmap.org/replication/%s/%s/%s/%s.state.txt" %\
            (time, sqnStr[0:3], sqnStr[3:6], sqnStr[6:9])

    if time == 'minute':
        end = 5
    else:
        end = 3

    u = requests.get(state_url)

    vals = u.text.encode('utf-8').split('\n')
    state = {}
    for val in vals[1:end]:
        (k, v) = val.split('=')
        state[k.lower()] = v.strip().replace("\\:", ":")

    info = (state['sequencenumber'], state['timestamp'], time, False)
    conn = connect()
    cur = conn.cursor()
    if reset == True:
        cur.execute("DELETE FROM file_list;")
        cur.execute("""INSERT INTO file_list
                       (sequence, timestamp, timetype, read)
                       VALUES (%s, %s, %s, %s);""", info)
    else:
        cur.execute("""UPDATE file_list SET
                       (sequence, timestamp, timetype, read)
                       VALUES (%s, %s, %s, %s);""", info)
    conn.commit()
