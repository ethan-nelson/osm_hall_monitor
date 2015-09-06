import connect
from sendNotification import sendNotification
from queries import *


def suspiciousFilter(changesets):
    whitelist = query_white_list()

    conn = connect.connect()
    cur = conn.cursor()

    for changesetid, changeset in changesets.iteritems():
        if changeset['username'] in whitelist:
            continue
        if changeset['delete'] > 0 and float(changeset['create'])/float(changeset['delete']) < 0.001:
            info = (changeset['timestamp'], changesetid,
                    changeset['username'].encode('utf8'),
                    1, float(changeset['create'])/float(changeset['delete']))
            cur.execute("""INSERT INTO history
                            (timestamp,changeset,username,flag,quantity)
                            VALUES (%s, %s, %s, %s, %s);""", info)
        if changeset['create'] > 1500:
            info = (changeset['timestamp'], changesetid,
                    changeset['username'].encode('utf8'),
                    2, changeset['create'])
            cur.execute("""INSERT INTO history
                            (timestamp,changeset,username,flag,quantity)
                            VALUES (%s, %s, %s, %s, %s);""", info)
        if changeset['delete'] > 1500:
            info = (changeset['timestamp'], changesetid,
                    changeset['username'].encode('utf8'),
                    3, changeset['create'])
            cur.execute("""INSERT INTO history
                            (timestamp,changeset,username,flag,quantity)
                            VALUES (%s, %s, %s, %s, %s);""", info)

    cur.execute("UPDATE filetime SET readflag = '%s';" % (True))
    conn.commit()


def userFilter(changesets):
    notifyList = []

    watchedUsers = query_user_list()

    conn = connect.connect()
    cur = conn.cursor()

    if watchedUsers:
        for changesetid, changeset in changesets.iteritems():
            for user in watchedUsers:
                if changeset['username'] == user:
                    info = (changeset['timestamp'], changesetid,
                            changeset['username'].encode('utf8'),
                            changeset['create'], changeset['modify'],
                            changeset['delete'])
                    cur.execute("""INSERT INTO user_history
                                (timestamp,changeset,username,added,changed,deleted)
                                VALUES (%s, %s, %s, %s, %s, %s);""", info)
                    notifyList.append([info].append(user))

        conn.commit()
    if notifyList:
        sendNotification(notifyList, 'user')    


def objectFilter(objects):
    notifyList = []

    watchedObjects = query_object_list()

    conn = connect.connect()
    cur = conn.cursor()

    if watchedObjects:
        for obj in watchedObjects:
            for node in objects.nodes.values():
                if 'n'+str(node['id']) == obj:
                    info = (node['timestamp'], node['changeset'],
                            node['username'].encode('utf8'),
                            node['action'], 'n'+str(node['id']))
                    cur.execute("""INSERT INTO object_history
                                    (timestamp,changeset,username,action,objectid)
                                    VALUES (%s, %s, %s, %s, %s);""", info)
                    notifyList.append(obj + [info])

            for way in objects.ways.values():
                if 'w'+str(way['id']) == obj:
                    info = (way['timestamp'], way['changeset'],
                            way['username'].encode('utf8'),
                            way['action'], 'w'+str(way['id']))
                    cur.execute("""INSERT INTO object_history
                                    (timestamp,changeset,username,action,objectid)
                                    VALUES (%s, %s, %s, %s, %s);""", info)
                    notifyList.append(obj + [info])

            for relation in objects.relations.values():
                if 'r'+str(relation['id']) == obj:
                    info = (relation['timestamp'], relation['changeset'],
                            relation['username'].encode('utf8'),
                            relation['action'], 'r'+str(relation['id']))
                    cur.execute("""INSERT INTO object_history
                                    (timestamp,changeset,username,action,objectid)
                                    VALUES (%s, %s, %s, %s, %s);""", info)
                    notifyList.append(obj + [info])

        conn.commit()
    if notifyList:
        sendNotification(notifyList, 'object')
