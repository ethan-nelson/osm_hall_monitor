from osmhm import connect, manage

def test_add_watched_user():
    manage.add_watched_user('testuser', 'Because', 'testadmin', 2, 'test@test.com')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_users;")
    results = cur.fetchall()

    assert len(results) == 1


def test_remove_watched_user():
    manage.remove_watched_user('testuser')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_users;")
    results = cur.fetchall()

    assert len(results) == 0


def test_add_watched_object():
    manage.add_watched_object('n322', 'Because', 'testadmin', 2, 'test@test.com')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_objects;")
    results = cur.fetchall()

    assert len(results) == 1


def test_remove_watched_object():
    manage.remove_watched_object('n322')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_objects;")
    results = cur.fetchall()

    assert len(results) == 0


def test_add_watched_key():
    manage.add_watched_key('railway', 'abandoned', 'Because', 'testadmin', 2, 'test@test.com')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_keys;")
    results = cur.fetchall()

    assert len(results) == 1


def test_remove_watched_key():
    manage.remove_watched_key('railway', 'abandoned')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_keys;")
    results = cur.fetchall()

    assert len(results) == 0
