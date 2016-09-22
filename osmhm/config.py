"""
config.py

Imports the local environment configuration parameters used in
  database access, event notification, and HTTP headers.

"""
import os
import warnings

http_headers = {'User-Agent': 'OSM Hall Monitor v0.3'}

try:
    database_url = os.environ['DATABASE_URL']
except:
    msg = 'No database_url detected; please set it with config.'
    warnings.warn(msg, UserWarning)

try:
    email_user = os.environ['EMAIL_USER']
except:
    msg = 'No email_user detected; please set it with config.'
    warnings.warn(msg, UserWarning)
