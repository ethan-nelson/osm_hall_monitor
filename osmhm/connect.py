import urlparse
import os
import psycopg2
from psycopg2.extras import DictCursor


def connect():
    urlparse.uses_netloc.append('postgres')
    dburl = urlparse.urlparse(os.environ['DATABASE_URL'])
    try:
        conn = psycopg2.connect(
            database=dburl.path[1:],
            user=dburl.username,
            password=dburl.password,
            host=dburl.hostname,
            port=dburl.port,
            cursor_factory=DictCursor,
            )
    except:
        print 'Error connecting to database!'
        return None
    return conn
