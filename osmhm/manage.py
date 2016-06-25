import connect


def add_watched_user(username, reason, author, email):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, reason, author, email)

    cur.execute("""INSERT INTO watched_users
                   (username, reason, author, email)
                   VALUES (%s, %s, %s, %s);""", info)

    conn.commit()


def remove_watched_user(username):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_users WHERE
                   username = %s;""", username)

    conn.commit()


def add_watched_user_object(username, reason, author, email):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, reason, author, email)

    cur.execute("""INSERT INTO watched_users_objects
                   (username, reason, author, email)
                   VALUES (%s, %s, %s, %s);""", info)


def remove_watched_user_object(username):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_users_objects WHERE
                   username = %s;""", username)


def add_watched_object(element, note, author, email):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (element, note, author, email)

    cur.execute("""INSERT INTO watched_objects
                   (element, reason, author, email)
                   VALUES (%s, %s, %s, %s);""", info)


    conn.commit()


def remove_watched_object(element):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_objects WHERE
                   element = %s;""", element)

    conn.commit()


def add_watched_key(key, value, note, author, email):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (key, value, note, author, email)

    cur.execute("""INSERT INTO watched_keys
                   (key, value, reason, author, email)
                   VALUES (%s, %s, %s, %s, %s);""", info)

    conn.commit()


def remove_watched_key(key, value):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM watched_keys WHERE
                   key = %s AND value = %s;""", (key, value))

    conn.commit()


def add_whitelisted_user(username, reason, author):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    info = (username, reason, author)

    cur.execute("""INSERT INTO whitelisted_users
                   (username, reason, author)
                   VALUES (%s, %s, %s);""", info)

    conn.commit()


def remove_whitelisted_user(username):
    """
    """
    conn = connect.connect()
    cur = conn.cursor()

    cur.execute("""DELETE FROM whitelisted_users WHERE
                   username = %s;""", username)

    conn.commit()
