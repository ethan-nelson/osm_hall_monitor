from osmhm import (
    connect,
    inserts,
    send_notification,
    queries,
)
import fnmatch


def suspicious_filter(changesets):
    """Set of rudimentary filters towards detecting possibly bad changesets.    

    1: Large amount of additions
    2: Large amount of modifications
    3: Large amount of deletions
    4: Large amount of combined actions
    5: High proportion of deletions
    6: High proportion of modifications
    """
    whitelist = queries.query_white_list()

    conn = connect.connect()
    cur = conn.cursor()

    for changesetid, changeset in changesets.iteritems():
        if changeset['username'] in whitelist:
            continue
        if changeset['create'] > 1500:
            info = (changeset['timestamp'], changesetid,
                    changeset['username'].encode('utf8'),
                    1, changeset['create'])
            cur.execute("""INSERT INTO history_filters
                            (timestamp,changeset,username,flag,quantity)
                            VALUES (%s, %s, %s, %s, %s);""", info)
        if changeset['modify'] > 1500:
            info = (changeset['timestamp'], changesetid,
                    changeset['username'].encode('utf8'),
                    2, changeset['modify'])
            cur.execute("""INSERT INTO history_filters
                            (timestamp,changeset,username,flag,quantity)
                            VALUES (%s, %s, %s, %s, %s);""", info)
        if changeset['delete'] > 1500:
            info = (changeset['timestamp'], changesetid,
                    changeset['username'].encode('utf8'),
                    3, changeset['delete'])
            cur.execute("""INSERT INTO history_filters
                            (timestamp,changeset,username,flag,quantity)
                            VALUES (%s, %s, %s, %s, %s);""", info)
        if changeset['create'] + changeset['modify'] + changeset['delete'] > 1500:
            info = (changeset['timestamp'], changesetid,
                    changeset['username'].encode('utf8'),
                    4, changeset['create'] + changeset['modify'] + changeset['delete'])
            cur.execute("""INSERT INTO history_filters
                            (timestamp,changeset,username,flag,quantity)
                            VALUES (%s, %s, %s, %s, %s);""", info)
        if changeset['delete'] > 0 and float(changeset['create']+changeset['modify'])/float(changeset['delete']) < 0.001:
            info = (changeset['timestamp'], changesetid,
                    changeset['username'].encode('utf8'),
                    5, float(changeset['create']+changeset['modify'])/float(changeset['delete']))
            cur.execute("""INSERT INTO history_filters
                            (timestamp,changeset,username,flag,quantity)
                            VALUES (%s, %s, %s, %s, %s);""", info)
        if changeset['modify'] > 0 and float(changeset['create']+changeset['delete'])/float(changeset['modify']) < 0.001:
            info = (changeset['timestamp'], changesetid,
                    changeset['username'].encode('utf8'),
                    6, float(changeset['create']+changeset['delete'])/float(changeset['modify']))
            cur.execute("""INSERT INTO history_filters
                            (timestamp,changeset,username,flag,quantity)
                            VALUES (%s, %s, %s, %s, %s);""", info)

    conn.commit()


def user_filter(changesets, notification=False, notifier=send_notification.basic_send_mail):
    notify_list = []

    watched_users = queries.query_user_list()

    conn = connect.connect()
    cur = conn.cursor()

    if watched_users:
        for changesetid, changeset in changesets.iteritems():
            for user in watched_users:
                if fnmatch.fnmatch(changeset['username'].encode('utf-8'), user['username']):
                    inserts.insert_user_event(changeset, user['id'])
                    notify_list.append({'timestamp': changeset['timestamp'], 'changesetid': changesetid,
                                        'username': changeset['username'].encode('utf8'), 'create': changeset['create'],
                                        'modify': changeset['modify'], 'delete': changeset['delete'], 'author': user['author'],
                                        'address': user['email'], 'reason': user['reason']})
    if notify_list and notification:
        send_notification.send_notification(notify_list, 'user', notifier=notifier)


def user_object_filter(objects, notification=False, notifier=send_notification.basic_send_mail):
    notify_list = []

    watched_users = queries.query_user_object_list()

    conn = connect.connect()
    cur = conn.cursor()

    if watched_users:
        for user in watched_users:
            for item_id, item in objects.iteritems():
                if fnmatch.fnmatch(item['username'].encode('utf-8'), user['username']):
                    if item['create'] == 1:
                        action = 'create'
                    elif item['modify'] == 1:
                        action = 'modify'
                    elif item['delete'] == 1:
                        action = 'delete'
                    for item_key in item['tags']:
                        info = (item['timestamp'], item['changeset'],
                        item['username'].encode('utf8'), action,
                        item_key, item['tags'][item_key])
                        cur.execute("""INSERT INTO history_users_objects
                                    (timestamp,changeset,username,action,key,value)
                                    VALUES (%s, %s, %s, %s, %s, %s);""", info)
        conn.commit()


def object_filter(objects, notification=False, notifier=send_notification.basic_send_mail):
    notify_list = []

    watched_objects = queries.query_object_list()

    conn = connect.connect()
    cur = conn.cursor()

    if watched_objects:
        for obj in watched_objects:
            for item_id, item in objects.iteritems():
                if item_id == obj['element']:
                    if item['create'] == 1:
                        item['action'] = 1
                    elif item['modify'] == 1:
                        item['action'] = 2
                    elif item['delete'] == 1:
                        item['action'] = 4
                    inserts.insert_object_event(item, obj['id'])
                    notify_list.append({'timestamp': item['timestamp'], 'changesetid': item['changeset'],
                                        'username': item['username'].encode('utf8'),
                                        'action': item['action'], 'element': item_id,
                                        'author': obj['author'], 'address': obj['email'], 'reason': obj['reason']})
    if notify_list and notification:
        send_notification.send_notification(notify_list, 'object', notifier=notifier)


def key_filter(objects, notification=False, notifier=send_notification.basic_send_mail):
    notify_list = []

    watched_keys = queries.query_key_list()

    conn = connect.connect()
    cur = conn.cursor()

    if watched_keys:
        for key in watched_keys:
            for item_id, item in objects.iteritems():
                for item_key in item['tags']:
                    if fnmatch.fnmatch(item_key,key['key']) and fnmatch.fnmatch(item['tags'][item_key],key['value']):
                        if item['create'] == 1:
                            item['action'] = 1
                        elif item['modify'] == 1:
                            item['action'] = 2
                        elif item['delete'] == 1:
                            item['action'] = 4
                        inserts.insert_key_event(item, item_key, key['id'])
                        notify_list.append({'timestamp': item['timestamp'], 'changesetid': item['changeset'],
                                            'username': item['username'].encode('utf8'), 'action': item['action'],
                                            'key': item_key, 'value': item['tags'][item_key],
                                            'author': item['author'], 'address': item['email'], 'reason': item['reason']})
    if notify_list and notification:
        send_notification.send_notification(notify_list, 'key', notifier=notifier)
