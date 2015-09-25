import os
import warnings


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
try:
    email_password = os.environ['EMAIL_PASS']
except:
    msg = 'No email_password detected; please set it with config.'
    warnings.warn(msg, UserWarning)
try:
    email_server = os.environ['EMAIL_SERVER']
except:
    msg = 'No email_server detected; please set it with config.'
    warnings.warn(msg, UserWarning)
