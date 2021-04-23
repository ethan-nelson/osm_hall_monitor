"""
manage.py

Functions that add or remove entries on tracking lists.

"""
from osmhm import connect


def add_watched_user(username, reason=None, author=None, authorid=None, email=None):
    """
    Add user to watched user list for tracking.

    Inputs
    ------
    username : str
        Username to track
    reason : str, optional
        Reason to track user
    author : str, optional
        User adding tracking entry
    authorid : int, optional
        Userid of user adding entry
    email : str, optional
        Email address for notification of events
    
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, reason, author, authorid, email)

    cur.execute("""INSERT INTO watched_users
                   (username, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s);""", info)

    conn.commit()


def remove_watched_user(username, authorid=None):
    """
    Remove user from tracking list associated with authorid.

    Inputs
    ------
    username : str
        Username to remove from database
    authorid : int, optional
        Userid of user adding entry
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, authorid)

    cur.execute("""DELETE FROM watched_users WHERE
                   username = %s and authorid = %s;""", info)

    conn.commit()


def add_watched_user_object(username, reason=None, author=None, authorid=None, email=None):
    """
    Add user to watched user list with object composites for tracking.

    Inputs
    ------
     username : str
        Username to track
    reason : str, optional
        Reason to track user
    author : str, optional
        User adding tracking entry
    authorid : int, optional
        Userid of user adding entry
    email : str, optional
        Email address for notification of events
    
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, reason, author, authorid, email)

    cur.execute("""INSERT INTO watched_users_objects
                   (username, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s);""", info)

    conn.commit()


def remove_watched_user_object(username, authorid=None):
    """
    Remove user from object composite user tracking list
    associated with authorid.
    
    Inputs
    ------
    username : str
        Username to remove from database
    authorid : int, optional
        Userid of user adding entry
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, authorid)

    cur.execute("""DELETE FROM watched_users_objects WHERE
                   username = %s and authorid = %s;""", info)

    conn.commit()


def add_watched_object(element, reason=None, author=None, authorid=None, email=None):
    """
    Add object to watched object list.

    Inputs
    ------
    element : str
        Object to track, with type specified as single letter
          prepended to object id (e.g. node 322 is 'n322')
    reason : str, optional
        Reason to track user
    author : str, optional
        User adding tracking entry
    authorid : int, optional
        Userid of user adding entry
    email : str, optional
        Email address for notification of events
 
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (element, reason, author, authorid, email)

    cur.execute("""INSERT INTO watched_objects
                   (element, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s);""", info)

    conn.commit()


def remove_watched_object(element, authorid=None):
    """
    Remove object from object tracking list associated with authorid.
    
    Inputs
    ------
    element : str
        Object to track, with type specified as single letter
          prepended to object id (e.g. node 322 is 'n322')
    authorid : int, optional
        Userid of user adding entry
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (element, authorid)

    cur.execute("""DELETE FROM watched_objects WHERE
                   element = %s and authorid = %s;""", info)

    conn.commit()


def add_watched_key(key, value, reason=None, author=None, authorid=None, email=None):
    """
    Add key/value combination to key/value tracking list.

    Inputs
    ------
    key : str
        Key to track; can be wildcard
    value : str
        Key value to track; can be wildcard
    reason : str, optional
        Reason to track user
    author : str, optional
        User adding tracking entry
    authorid : int, optional
        Userid of user adding entry
    email : str, optional
        Email address for notification of events
 
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (key, value, reason, author, authorid, email)

    cur.execute("""INSERT INTO watched_keys
                   (key, value, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s, %s);""", info)

    conn.commit()


def remove_watched_key(key, value, authorid=None):
    """
    Remove object from object tracking list associated with authorid.
    
    Inputs
    ------
    key : str
        Key to remove
    value : str
        Key value to remove
    authorid : int, optional
        Userid of user adding entry
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (key, value, authorid)

    cur.execute("""DELETE FROM watched_keys WHERE
                   key = %s and value = %s and authorid = %s;""", info)

    conn.commit()


def add_whitelisted_user(username, reason=None, author=None, authorid=None):
    """
    Add whitelisted user that is not picked up in tracking.

    Inputs
    ------
    username : str
        Username to track
    reason : str, optional
        Reason to track user
    author : str, optional
        User adding tracking entry
    authorid : int, optional
        Userid of user adding entry
 
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, reason, author, authorid)

    cur.execute("""INSERT INTO whitelisted_users
                   (username, reason, author, authorid)
                   VALUES (%s, %s, %s, %s);""", info)

    conn.commit()


def remove_whitelisted_user(username, authorid=None):
    """
    Remove whitelisted user from untracked list.

    Inputs
    ------
    username : str
        Username to remove
    authorid : int, optional
        Userid of user adding entry
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, authorid)

    cur.execute("""DELETE FROM whitelisted_users WHERE
                   username = %s and authorid = %s;""", info)

    conn.commit()


def add_last_file(sequence, timestamp, timetype, read):
    """
    Add information about the last state file seen.
    
    Inputs
    ------
    sequence : int
        Sequence number of state file
    timestamp : str
        Stringified timestamp from file
    timetype : str
        Time resolution of state file
    read : bool
        Flag indicating if file has been read or not
    
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""INSERT INTO file_list 
                   (username, reason, author, authorid)
                   VALUES (%s, %s, %s, %s);""", info)

    conn.commit()


def get_last_file():
    """
    Retrieve information about the last state file seen.
    
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM file_list;")
    return cur.fetchone()


def update_last_file(sequence, timestamp, timetype, read):
    """
    Update information about the last state file seen.
    
    Inputs
    ------
    sequence : int
        Sequence number of state file
    timestamp : str
        Stringified timestamp from file
    timetype : str
        Time resolution of state file
    read : bool
        Flag indicating if file has been read or not
    
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("""UPDATE file_list SET 
                   (username, reason, author, authorid)
                   = (%s, %s, %s, %s);""", info)

    conn.commit()


def remove_last_file():
    """
    Remove the last file information.
    
    """
    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM file_list;")

    conn.commit()
