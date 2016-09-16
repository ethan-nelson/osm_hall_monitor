import connect


def add_watched_user(username, reason, author, authorid, email):
    """
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
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_users WHERE
                   username = %s;""", username)

    conn.commit()


def add_watched_user_object(username, reason, author, authorid, email):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, reason, author, authorid, email)

    cur.execute("""INSERT INTO watched_users_objects
                   (username, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s);""", info)


def remove_watched_user_object(username):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_users_objects WHERE
                   username = %s;""", username)


def add_watched_object(element, note, author, authorid, email):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (element, note, author, authorid, email)

    cur.execute("""INSERT INTO watched_objects
                   (element, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s);""", info)


    conn.commit()


def remove_watched_object(element):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_objects WHERE
                   element = %s;""", element)

    conn.commit()


def add_watched_key(key, value, note, author, authorid, email):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (key, value, note, author, authorid, email)

    cur.execute("""INSERT INTO watched_keys
                   (key, value, reason, author, authorid, email)
                   VALUES (%s, %s, %s, %s, %s, %s);""", info)

    conn.commit()


def remove_watched_key(key, value):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_keys WHERE
                   key = %s AND value = %s;""", (key, value))

    conn.commit()


def add_whitelisted_user(username, reason, author, authorid):
    """
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
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM whitelisted_users WHERE
                   username = %s;""", username)

    conn.commit()
