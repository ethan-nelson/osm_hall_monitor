from osmhm import connect, manage

def test_add_watched_user():
    manage.add_watched_user('testuser', 'Because', 'testadmin', 2, 'test@test.com')

    conn = connect.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watched_users;")
    results = cur.fetchall()

    assert len(results) == 1
