import connect


def query_white_list():
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM whitelist")
    white_list = cur.fetchall()
    whitelist = [name[0] for name in white_list]

    return white_list

def query_user_list():
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users")
    watched_users = cur.fetchall()
    watched_users = [name[0] for name in watched_users]

    return watched_users

def query_object_list():
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("SELECT number FROM objects")
    watched_objects = cur.fetchall()
    watched_objects = [name[0] for name in watched_objects]

    return watched_objects

def query_block_list():
    pass
