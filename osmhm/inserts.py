from osmhm import connect


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
