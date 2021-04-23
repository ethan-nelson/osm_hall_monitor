from osmhm import connect, inserts, db

def test_add_watched_user():
    db.add_watched_user('testuser', 'Because', 'testadmin', 2, 'test@test.com')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_users;")
    results = cur.fetchall()

    assert len(results) == 1


def test_add_watched_user_minimal_details():
    db.add_watched_user('testuser2')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_users;")
    results = cur.fetchall()

    assert len(results) == 2


def test_remove_watched_user():
    db.remove_watched_user('testuser')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_users;")
    results = cur.fetchall()

    assert len(results) == 1


def test_add_watched_object():
    db.add_watched_object('n322', 'Because', 'testadmin', 2, 'test@test.com')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_objects;")
    results = cur.fetchall()

    assert len(results) == 1


def test_add_watched_object_minimal_details():
    db.add_watched_object('n323')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_objects;")
    results = cur.fetchall()

    assert len(results) == 2


def test_remove_watched_object():
    db.remove_watched_object('n322')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_objects;")
    results = cur.fetchall()

    assert len(results) == 1


def test_add_watched_key():
    db.add_watched_key('railway', 'abandoned', 'Because', 'testadmin', 2, 'test@test.com')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_keys;")
    results = cur.fetchall()

    assert len(results) == 1

def test_add_watched_key_minimal_details():
    db.add_watched_key('railway', 'rail')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_keys;")
    results = cur.fetchall()

    assert len(results) == 2


def test_remove_watched_key():
    db.remove_watched_key('railway', 'abandoned')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_keys;")
    results = cur.fetchall()

    assert len(results) == 1


def test_insert_user_event():
    inserts.insert_user_event({'id': 1,
                              'timestamp': '2018-01-01T00:00:00Z',
                              'uid': 2,
                              'create': 1,
                              'modify': 2,
                              'delete': 0}, 1)

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM history_users;")
    results = cur.fetchall()

    assert len(results) == 1


def test_prune_user_event():
    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM history_users;")
    results = cur.fetchall()

    assert len(results) == 1

    cur.execute("""DELETE FROM history_users WHERE TO_TIMESTAMP(timestamp, 'YYYY-MM-DDTHH:MI:SSZ') < NOW() - INTERVAL '30 days';""")
    conn.commit()

    cur.execute("SELECT * FROM history_users;")
    results = cur.fetchall()

    assert len(results) == 0


def test_insert_object_event():
    inserts.insert_object_event({'timestamp': '2018-01-01T00:00:00Z',
                                 'username': 'testuser',
                                 'uid': 2,
                                 'action': 1,
                                 'changeset': 20}, 10)

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM history_objects;")
    results = cur.fetchall()

    assert len(results) == 1


def test_prune_object_event():
    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM history_objects;")
    results = cur.fetchall()

    assert len(results) == 1

    cur.execute("""DELETE FROM history_objects WHERE TO_TIMESTAMP(timestamp, 'YYYY-MM-DDTHH:MI:SSZ') < NOW() - INTERVAL '30 days';""")
    conn.commit()

    cur.execute("SELECT * FROM history_objects;")
    results = cur.fetchall()

    assert len(results) == 0


def test_insert_key_event():
    inserts.insert_key_event({'id': 'n20',
                              'timestamp': '2018-01-01T00:00:00Z',
                              'username': 'testuser',
                              'uid': 2,
                              'action': 2,
                              'tags': {'railway': 'abandoned'},
                              'changeset': 21}, 'railway', 12)

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM history_keys;")
    results = cur.fetchall()

    assert len(results) == 1


def test_prune_key_event():
    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM history_keys;")
    results = cur.fetchall()

    assert len(results) == 1

    cur.execute("""DELETE FROM history_keys WHERE TO_TIMESTAMP(timestamp, 'YYYY-MM-DDTHH:MI:SSZ') < NOW() - INTERVAL '30 days';""")
    conn.commit()

    cur.execute("SELECT * FROM history_keys;")
    results = cur.fetchall()

    assert len(results) == 0
