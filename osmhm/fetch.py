from connect import connect
import requests


def fetchLast():
    conn = connect()
    if conn:
        cur = conn.cursor()

        sequence = {}
        cur.execute("SELECT * FROM filetime;")
        foo, sequence['sequencenumber'], sequence['timestamp'], \
            readflag = cur.fetchone()

        return sequence, readflag
    else:
        return None, None


def fetchNext(currentSequence):
    nextSequence = int(currentSequence['sequencenumber']) + 1
    sqnStr = str(nextSequence).zfill(9)
    stateUrl = "http://planet.openstreetmap.org/replication/hour/%s/%s/%s.state.txt" %\
        (sqnStr[0:3], sqnStr[3:6], sqnStr[6:9])

    try:
        u = requests.get(stateUrl)

        vals = u.text.encode('utf-8').split('\n')
        state = {}
        for val in vals[1:3]:
            (k, v) = val.split('=')
            state[k.lower()] = v.strip().replace("\\:", ":")

        conn = connect()
        if conn:
            cur = conn.cursor()
            cur.execute("UPDATE filetime SET sequencenumber = '%s', timestamp = '%s', readflag = '%s';" %
                        (state['sequencenumber'], state['timestamp'], False))
            conn.commit()
        else:
            return False
    except:
        return False

    return True
