from connect import connect
import urllib2


def fetchLast():
    conn = connect()
    if conn:
        cur = conn.cursor()

        sequence = {}
        cur.execute("SELECT * FROM filetime;")
        foo, sequence['number'], sequence['timestamp'], \
            readflag = cur.fetchone()

        return sequence, readflag
    else:
        return None, None


def fetchNext(currentSequence):
    nextSequence = int(currentSequence['number']) + 1
    sqnStr = str(nextSequence).zfill(9)
    url = "http://planet.openstreetmap.org/replication/hour/%s/%s/%s.state.txt" %\
        (sqnStr[0:3], sqnStr[3:6], sqnStr[6:9])
    try:
        u = urllib2.urlopen(url)

        conn = connect()
        cur = conn.cursor()

        vals = u.read().split('\n')
        state = {}
        for val in vals[1:3]:
            (k, v) = val.split('=')
            state[k.lower()] = v.strip().replace("\\:", ":")

        cur.execute("UPDATE filetime SET sequencenumber = '%s', timestamp = '%s', readflag = '%s';" %
                    (state['number'], state['timestamp'], False))
        conn.commit()

    except:
        return False

    return True
