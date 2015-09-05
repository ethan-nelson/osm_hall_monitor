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


