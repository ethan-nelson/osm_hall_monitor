from osmhm import connect


error_message = 'Action is not defined. Please use create, truncate, or drop.'
def file_list(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE file_list (
              id SERIAL NOT NULL PRIMARY KEY,
              sequence TEXT,
              timestamp TEXT,
              timetype TEXT,
              read BOOLEAN
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
              TRUNCATE TABLE file_list;
              """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
              DROP TABLE file_list;
              """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def history_users(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE history_users (
              id SERIAL NOT NULL PRIMARY KEY,
              wid INTEGER NOT NULL,
              userid BIGINT NOT NULL,
              changeset BIGINT NOT NULL,
              timestamp TEXT NOT NULL,
              created BIGINT,
              modified BIGINT,
              deleted BIGINT
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE history_users;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE history_users;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def history_all_users(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE history_all_users (
              id SERIAL NOT NULL PRIMARY KEY,
              username TEXT NOT NULL,
              changeset TEXT NOT NULL,
              timestamp TEXT NOT NULL,
              created TEXT,
              modified TEXT,
              deleted TEXT
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE history_all_users;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE history_all_users;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def history_all_changesets(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE history_all_changesets (
              id SERIAL NOT NULL PRIMARY KEY,
              changeset TEXT NOT NULL,
              username TEXT NOT NULL,
              timestamp TEXT NOT NULL,
              created TEXT,
              modified TEXT,
              deleted TEXT
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE history_all_changesets;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE history_all_changesets;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def history_users_objects(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE history_users_objects (
              id SERIAL NOT NULL PRIMARY KEY,
              key TEXT NOT NULL,
              value TEXT NOT NULL,
              username TEXT NOT NULL,
              changeset BIGINT NOT NULL,
              timestamp TEXT NOT NULL,
              action TEXT
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE history_users_objects;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE history_users_objects;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def history_objects(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE history_objects (
              id SERIAL NOT NULL PRIMARY KEY,
              wid INTEGER NOT NULL,
              userid BIGINT NOT NULL,
              username TEXT NOT NULL,
              changeset BIGINT NOT NULL,
              timestamp TEXT NOT NULL,
              action SMALLINT NOT NULL
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE history_objects;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE history_objects;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def history_keys(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE history_keys (
              id SERIAL NOT NULL PRIMARY KEY,
              wid INTEGER NOT NULL,
              userid BIGINT NOT NULL,
              key TEXT NOT NULL,
              value TEXT NOT NULL,
              element TEXT NOT NULL,
              username TEXT NOT NULL,
              changeset BIGINT NOT NULL,
              timestamp TEXT NOT NULL,
              action SMALLINT NOT NULL
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE history_keys;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE history_keys;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def history_filters(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE history_filters (
              id SERIAL NOT NULL PRIMARY KEY,
              flag INT NOT NULL,
              username TEXT NOT NULL,
              changeset BIGINT NOT NULL,
              timestamp TEXT NOT NULL,
              quantity TEXT NOT NULL
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE history_filters;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE history_filters;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def watched_users(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE watched_users (
              id SERIAL NOT NULL PRIMARY KEY,
              userid BIGINT,
              username TEXT NOT NULL,
              reason TEXT,
              author TEXT,
              authorid BIGINT,
              email TEXT
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE watched_users;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE watched_users;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def watched_users_objects(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE watched_users_objects (
              id SERIAL NOT NULL PRIMARY KEY,
              username TEXT NOT NULL,
              reason TEXT,
              author TEXT,
              authorid BIGINT,
              email TEXT
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE watched_users_objects;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE watched_users_objects;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def watched_objects(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE watched_objects (
              id SERIAL NOT NULL PRIMARY KEY,
              element TEXT NOT NULL,
              reason TEXT,
              author TEXT,
              authorid BIGINT,
              email TEXT
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE watched_objects;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE watched_objects;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def watched_keys(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE watched_keys (
              id SERIAL NOT NULL PRIMARY KEY,
              key TEXT NOT NULL,
              value TEXT NOT NULL,
              reason TEXT,
              author TEXT,
              authorid BIGINT,
              email TEXT
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE watched_keys;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE watched_keys;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def whitelisted_users(action):
    conn = connect.connect()
    cur = conn.cursor()
    if action in ['create', 'c']:
        cur.execute("""
            CREATE TABLE whitelisted_users (
              id SERIAL NOT NULL PRIMARY KEY,
              username TEXT NOT NULL,
              reason TEXT,
              author TEXT,
              authorid BIGINT
            );
            """)
    elif action in ['truncate', 't']:
        cur.execute("""
            TRUNCATE TABLE whitelisted_users;
            """)
    elif action in ['drop', 'delete', 'd']:
        cur.execute("""
            DROP TABLE whitelisted_users;
            """)
    else:
        raise NotImplementedError(error_message)
    conn.commit()


def all_tables(action):
    if action in ['create', 'c']:
        message = "You are about to create all tables for OSM Hall Monitor. Are you sure? (Y or N): "
    elif action in ['truncate', 't']:
        message = "You are about to truncate all tables but the file list for OSM Hall Monitor. Are you sure? (Y or N): "
        second_message = "Would you like to truncate the file list table as well? (Y or N): "
    elif action in ['drop', 'delete', 'd']:
        message = "You are about to drop all tables for OSM Hall Monitor. Are you sure? (Y or N): "
    else:
        raise NotImplementedError(error_message)

    response = str(raw_input(message))

    if response.lower() not in ['y', 'yes']:
        print('Execution halted.')
        return

    if action in ['truncate', 't']:
        response = str(raw_input(second_message))
        if response.lower() not in ['y', 'yes']:
            pass
        else:
            file_list(action)
    else:
        file_list(action)

    history_users(action)
    history_users_objects(action)
    history_all_users(action)
    history_all_changesets(action)
    history_objects(action)
    history_keys(action)
    history_filters(action)
    watched_users(action)
    watched_users_objects(action)
    watched_objects(action)
    watched_keys(action)
    whitelisted_users(action)

    print('Done.')
