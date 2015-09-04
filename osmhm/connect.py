import urlparse
import os
import psycopg2
from psycopg2.extras import DictCursor


def connect():
    urlparse.uses_netloc.append('postgres')
    db_url = urlparse.urlparse(os.environ['DATABASE_URL'])
    try:
        connection = psycopg2.connect(
            database=db_url.path[1:],
            user=db_url.username,
            password=db_url.password,
            host=db_url.hostname,
            port=db_url.port,
            cursor_factory=DictCursor,
            )
    except:
        raise Exception('Error connecting to database!')
    return connection
