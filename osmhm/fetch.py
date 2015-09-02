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


def fetchThis(currentSequence, time='hour'):
    import StringIO
    import gzip

    try:
        sqn = str(currentSequence).zfill(9)
        url = "http://planet.osm.org/replication/%s/%s/%s/%s.osc.gz" %\
              (time, sqn[0:3], sqn[3:6], sqn[6:9])

        content = requests.get(url)
        content = StringIO.StringIO(content.content)
        dataStream = gzip.GzipFile(fileobj=content)

        return dataStream
    except:
        return None


def fetchNext(currentSequence, time='hour'):
    nextSequence = int(currentSequence) + 1
    sqnStr = str(nextSequence).zfill(9)
    stateUrl = "http://planet.openstreetmap.org/replication/%s/%s/%s/%s.state.txt" %\
        (time, sqnStr[0:3], sqnStr[3:6], sqnStr[6:9])

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
