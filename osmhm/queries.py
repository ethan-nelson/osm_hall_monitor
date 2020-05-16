"""
queries.py

Retrieves lists of entries on tracking lists and do-not-track lists.

"""
from osmhm import connect


def query_white_list():
    """
    Retrieve list of users on whitelist.

    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM whitelisted_users")
    white_list = cur.fetchall()
    whitelist = [name[0] for name in white_list]

    return white_list


def query_user_list():
    """
    Retrieve list of users on user watch list.

    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM watched_users")
    watched_users = cur.fetchall()

    return watched_users


def query_user_object_list():
    """
    Retrieve list of users on object composite watch list.

    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM watched_users_objects")
    watched_users = cur.fetchall()

    return watched_users


def query_object_list():
    """
    Retrieve list of objects on object watch list.

    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM watched_objects")
    watched_objects = cur.fetchall()

    return watched_objects


def query_key_list():
    """
    Retrieve list of key/value pairs on key/value pair list.

    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM watched_keys")
    watched_keys = cur.fetchall()

    return watched_keys
