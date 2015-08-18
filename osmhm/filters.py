from connect import connect
from sendNotification import sendNotification


def suspiciousFilter(changesets):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM whitelist")
    whitelist = cur.fetchall()

    for changesetid, changeset in changesets.iteritems():
        if changeset['username'] in whitelist:
            continue
        if 'create' in changeset and 'delete' in changeset\
                and float(changeset['create'])/float(changeset['delete']) < 0.001:
            cur.execute("""INSERT INTO history\
                            (timestamp,changeset,username,flag,quantity)\
                            VALUES (%s, %s, %s, %s, %s);""",
                        (changeset['timestamp'], changesetid,
                         changeset['username'].encode('utf8'),
                         1, float(changeset['create'])/float(changeset['delete']))
                        )
        if 'create' in changeset and changeset['create'] > 1500:
            cur.execute("""INSERT INTO history\
                            (timestamp,changeset,username,flag,quantity)\
                            VALUES (%s, %s, %s, %s, %s);""",
                        (changeset['timestamp'], changesetid,
                         changeset['username'].encode('utf8'),
                         2, changeset['create'])
                        )
        if 'delete' in changeset and changeset['delete'] > 1500:
            cur.execute("""INSERT INTO history\
                            (timestamp,changeset,username,flag,quantity)\
                            VALUES (%s, %s, %s, %s, %s);""",
                        (changeset['timestamp'], changesetid,
                         changeset['username'].encode('utf8'),
                         3, changeset['delete'])
                        )

    cur.execute("UPDATE filetime SET readflag = '%s';" % (True))
    conn.commit()


def userFilter(changesets):
    notifyList = []
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    watchedUsers = cur.fetchall()

    if watchedUsers:
        for changesetid, changeset in changesets.iteritems():
            for user in watchedUsers:
                if changeset['username'] == user['username']:
                    if 'create' not in changeset:
                        changeset['create'] = 0
                    if 'modify' not in changeset:
                        changeset['modify'] = 0
                    if 'delete' not in changeset:
                        changeset['delete'] = 0
                    cur.execute("""INSERT INTO user_history\
                                (timestamp,changeset,username,added,changed,deleted)\
                                VALUES (%s, %s, %s, %s, %s, %s);""",
                            (changeset['timestamp'], changesetid,
                             changeset['username'].encode('utf8'),
                             changeset['create'], changeset['modify'],
                             changeset['delete'])
                            )
                    notifyList.append(user + [changeset['timestamp'], changesetid,\
                                 changeset['username'].encode('utf8'), changeset['create'],\
                                 changeset['modify'], changeset['delete']])
        conn.commit()
    if notifyList:
        sendNotification(notifyList, 'user')    


def objectFilter(objects):
    notifyList = []
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM objects")
    watchedObjects = cur.fetchall()

    if watchedObjects:
        for obj in watchedObjects:
            for node in objects.nodes.values():
                if 'n'+str(node['id']) == obj['number']:
                    cur.execute("""INSERT INTO object_history\
                                    (timestamp,changeset,username,action,objectid)\
                                    VALUES (%s, %s, %s, %s, %s);""",
                                (node['timestamp'], node['changeset'],
                                 node['username'].encode('utf8'),
                                 node['action'], 'n'+str(node['id']))
                                )
                    notifyList.append(obj + [node['timestamp'], str(node['changeset']),
                                 node['username'].encode('utf8'), 'n' + str(node['id']),
                                 node['action']])
            for way in objects.ways.values():
                if 'w'+str(way['id']) == obj['number']:
                    cur.execute("""INSERT INTO object_history\
                                    (timestamp,changeset,username,action,objectid)\
                                    VALUES (%s, %s, %s, %s, %s);""",
                                (way['timestamp'], way['changeset'],
                                 way['username'].encode('utf8'),
                                 way['action'], 'w'+str(way['id']))
                                )
                    notifyList.append(obj + [way['timestamp'], way['changeset'],
                                 way['username'].encode('utf8'), 'w'+str(way['id']),
                                 way['action']])
            for relation in objects.relations.values():
                if 'r'+str(relation['id']) == obj['number']:
                    cur.execute("""INSERT INTO object_history\
                                    (timestamp,changeset,username,action,objectid)\
                                    VALUES (%s, %s, %s, %s, %s);""",
                                (relation['timestamp'], relation['changeset'],
                                 relation['username'].encode('utf8'),
                                 relation['action'], 'r'+str(relation['id']))
                                )
                    notifyList.append(obj + [relation['timestamp'], relation['changeset'],
                                 relation['username'].encode('utf8'), 'r' + str(relation['id']),
                                 relation['action']])
        conn.commit()
    if notifyList:
        sendNotification(notifyList, 'object')
