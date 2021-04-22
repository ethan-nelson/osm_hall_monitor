"""
manage.py

Functions that add or remove entries on tracking lists.

"""
from osmhm import connect


def add_watched_user(username, reason, author, authorid, email):
    """
    Add user to watched user list for tracking.

    Inputs
    ------
    username : str
        Username to track
    reason : str
        Reason to track user
    author : str
        User adding tracking entry
    authorid : int
        Userid of user adding entry
    email : str, option
        Email address for notification of events
    
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, reason, author, authorid, email)

    cur.execute("""INSERT INTO watched_users
                   (username, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s);""", info)

    conn.commit()


def remove_watched_user(username):
    """
    Remove user from tracking list.

    Inputs
    ------
    username : str
        Username to remove from database
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_users WHERE
                   username = %s;""", (username,))

    conn.commit()


def add_watched_user_object(username, reason, author, authorid, email):
    """
    Add user to watched user list with object composites for tracking.

    Inputs
    ------
     username : str
        Username to track
    reason : str
        Reason to track user
    author : str
        User adding tracking entry
    authorid : int
        Userid of user adding entry
    email : str, option
        Email address for notification of events
    
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, reason, author, authorid, email)

    cur.execute("""INSERT INTO watched_users_objects
                   (username, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s);""", info)


def remove_watched_user_object(username):
    """
    Remove user from object composite user tracking list.
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_users_objects WHERE
                   username = %s;""", (username,))


def add_watched_object(element, reason, author, authorid, email):
    """
    Add object to watched object list.

    Inputs
    ------
    element : str
        Object to track, with type specified as single letter
          prepended to object id (e.g. node 322 is 'n322')
    reason : str
        Reason to track user
    author : str
        User adding tracking entry
    authorid : int
        Userid of user adding entry
    email : str, option
        Email address for notification of events
 
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (element, reason, author, authorid, email)

    cur.execute("""INSERT INTO watched_objects
                   (element, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s);""", info)


    conn.commit()


def remove_watched_object(element):
    """
    Remove object from object tracking list.
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_objects WHERE
                   element = %s;""", (element,))

    conn.commit()


def add_watched_key(key, value, reason, author, authorid, email):
    """
    Add key/value combination to key/value tracking list.

    Inputs
    ------
    key : str
        Key to track; can be wildcard
    value : str
        Key value to track; can be wildcard
    reason : str
        Reason to track user
    author : str
        User adding tracking entry
    authorid : int
        Userid of user adding entry
    email : str, option
        Email address for notification of events
 
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (key, value, reason, author, authorid, email)

    cur.execute("""INSERT INTO watched_keys
                   (key, value, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s, %s);""", info)

    conn.commit()


def remove_watched_key(key, value):
    """
    Remove key/value combination from key/value tracking list.

    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_keys WHERE
                   key = %s AND value = %s;""", (key, value))

    conn.commit()


def add_whitelisted_user(username, reason, author, authorid):
    """
    Add whitelisted user that is not picked up in tracking.

    Inputs
    ------
    username : str
        Username to track
    reason : str
        Reason to track user
    author : str
        User adding tracking entry
    authorid : int
        Userid of user adding entry
 
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, reason, author, authorid)

    cur.execute("""INSERT INTO whitelisted_users
                   (username, reason, author, authorid)
                   VALUES (%s, %s, %s, %s);""", info)

    conn.commit()


def remove_whitelisted_user(username):
    """
    Remove whitelisted user from untracked list.

    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM whitelisted_users WHERE
                   username = %s;""", (username,))

    conn.commit()
