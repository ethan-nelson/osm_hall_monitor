import connect


def query_white_list():
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM whitelisted_users")
    white_list = cur.fetchall()
    whitelist = [name[0] for name in white_list]

    return white_list

def query_user_list():
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM watched_users")
    watched_users = cur.fetchall()

    return watched_users

def query_object_list():
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM watched_objects")
    watched_objects = cur.fetchall()

    return watched_objects

def query_block_list():
    pass
