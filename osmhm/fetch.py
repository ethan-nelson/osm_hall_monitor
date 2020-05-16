"""
fetch.py

Contains functions to fetch diff file information (state files) from
  OpenStreetMap (OSM) planet server.

"""
from osmhm import config
from osmhm.connect import connect
import requests


def fetch_last_read():
    """
    Accesses the file_list table to retrieve the most recently read
      diff file as well as information about it. If the file listing
      does not contain any information, it returns None.

    """
    conn = connect()
    cur = conn.cursor()

    cur = conn.cursor()
    cur.execute("SELECT * FROM file_list;")

    try:
        sequence = {}
        _, sequence['sequencenumber'], sequence['timestamp'], \
            sequence['timetype'], sequence['read_flag'] = cur.fetchone()

        return sequence
    except:
        return None


def fetch_next(current_sequence='', time_type='hour', reset=False):
    """
    Given a current sequence, fetches information about the next
      diff file from its state file. If no sequence has been read
      before, can fetch information for the most recent one. Once
      fetched, file_list table is updated with this information.

    Inputs
    ------
    current_sequence : float or int
        Up to nine digit number corresponding to the last read
          sequence by the system. Inputs less than 9 digits are
          left-padded with zeros.

    time_type : {'minute', 'hour', 'day'}
        Time resolution of diff files desired.

    reset : bool
        Flag to retrieve latest diff sequence state from OSM and
          clear old file listing in database if it exists.

    """
    if reset is True:
        state_url = ("https://planet.openstreetmap.org/replication/"
                     "%s/state.txt") % (time_type)

    else:
        next_sequence = int(current_sequence) + 1
        sequence_string = str(next_sequence).zfill(9)
        state_url = ("https://planet.openstreetmap.org/replication/"
                     "%s/%s/%s/%s.state.txt") % (time_type,
                         sequence_string[0:3], sequence_string[3:6],
                         sequence_string[6:9])

    if time_type == 'minute':
        end = 5
    else:
        end = 3

    response = requests.get(state_url, headers=config.http_headers)

    if response.status_code == 404:
        raise Exception('Unable to reach OpenStreetMap server.')

    state = {}
    vals = response.text.encode('utf-8').split('\n')

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
