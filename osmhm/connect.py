"""
connect.py

Provides a connection to the database.

"""
from osmhm import config
import psycopg2
from psycopg2.extras import DictCursor
try:
    import urlparse
except:
    import urllib.parse as urlparse


def connect():
    """
    Creates a connection object for the database. This function uses
      the variable osmhm.config.database_url as the database address.
      Only PostgreSQL support is available at this time.

    """
    urlparse.uses_netloc.append('postgres')
    db_url = urlparse.urlparse(config.database_url)

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
        raise Exception("""Error connecting to database! Please check
                           the database configuration variable.""")

    return connection
