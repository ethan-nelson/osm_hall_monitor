from osmhm import connect


def insert_file_read():
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("UPDATE file_list SET read = '%s';", (True,))
    conn.commit()


def insert_user_event(changeset, wid):
    conn = connect.connect()
    cur = conn.cursor()

    info = (wid, changeset['id'], changeset['timestamp'], changeset['uid'],
            changeset['create'], changeset['modify'], changeset['delete'])
    cur.execute("""INSERT INTO history_users
                    (wid, changeset, timestamp, userid, created, modified, \
                    deleted) VALUES (%s, %s, %s, %s, %s, %s, %s);""", info)
    conn.commit()


def insert_object_event(object, wid):
    conn = connect.connect()
    cur = conn.cursor()

    info = (wid, object['timestamp'],
            object['username'].encode('utf8'), object['uid'],
            object['action'], object['changeset'])
    cur.execute("""INSERT INTO history_objects
                    (wid, timestamp, username, userid, action, changeset)
                    VALUES (%s, %s, %s, %s, %s, %s);""", info)
    conn.commit()


def insert_key_event(object, key, wid):
    conn = connect.connect()
    cur = conn.cursor()

    info = (wid, object['id'], object['timestamp'],
            object['username'].encode('utf8'), object['uid'],
            object['action'], key, object['tags'][key],
            object['changeset'])
    cur.execute("""INSERT INTO history_keys
                    (wid, element, timestamp, username, userid, action, key, 
                    value, changeset) VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s);""", info)
    conn.commit()


def insert_all_users(users):
    conn = connect.connect()
    cur = conn.cursor()

    for username, user in users.iteritems():
        info = (username, user["changesets"], user["timestamps"],
                    user["action"]["create"], user["action"]["modify"],
                    user["action"]["delete"])
        cur.execute("""INSERT INTO history_all_users
                        (username, changeset, timestamp, created, modified, deleted)
                        VALUES (%s, %s, %s, %s, %s, %s);""", info)

    conn.commit()


def insert_all_changesets(changesets):
    conn = connect.connect()
    cur = conn.cursor()

    for changesetid, changeset in changesets.iteritems():
        info = (changesetid, changeset["username"], changeset["timestamp"],
                    changeset["create"], changeset["modify"],
                    changeset["delete"])
        cur.execute("""INSERT INTO history_all_changesets
                       (changeset, username, timestamp, created, modified, deleted)
                       VALUES (%s, %s, %s, %s, %s, %s);""", info)

    conn.commit()
