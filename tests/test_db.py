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


def test_remove_watched_user_by_wrong_authorid():
    db.remove_watched_user('testuser', 1)

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_users;")
    results = cur.fetchall()

    assert len(results) == 2


def test_remove_watched_user_by_authorid():
    db.remove_watched_user('testuser', 2)

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


def test_remove_watched_object_by_wrong_authorid():
    db.remove_watched_object('n322', 1)

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_objects;")
    results = cur.fetchall()

    assert len(results) == 2

def test_remove_watched_object_by_authorid():
    db.remove_watched_object('n322', 2)

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_objects;")
    results = cur.fetchall()

    assert len(results) == 1


def test_add_watched_key():
    db.add_watched_key('railway', 'abandoned', 'Because', 'testnonadmin', 3, 'test@test.com')

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


def test_remove_watched_key_by_wrong_authorid():
    db.remove_watched_key('railway', 'abandoned', 2)

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_keys;")
    results = cur.fetchall()

    assert len(results) == 2


def test_remove_watched_key_by_authorid():
    db.remove_watched_key('railway', 'abandoned', 3)

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


def test_add_last_file():
    db.add_last_file('001002003', '2020-01-01T06:14:01Z', 'hour', False)

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM file_list;")
    results = cur.fetchall()

    assert len(results) == 1


def test_get_last_file():
    db_results = db.get_last_file()
    assert len(results) == 1

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM file_list;")
    test_results = cur.fetchall()

    assert db_results == test_results


def test_update_last_file():
    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM file_list;")
    old_results = cur.fetchall()

    db.update_last_file('001002004', '2020-01-01T07:14:05Z', 'hour', False)

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM file_list;")
    new_results = cur.fetchall()

    assert len(new_results) == 1
    assert old_results != new_results


def test_remove_last_file():
    db.remove_last_file()

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM file_list;")
    results = cur.fetchall()

    assert len(results) == 0
