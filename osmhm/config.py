import os
import urlparse
import warnings


try:
    database_url = os.environ['DATABASE_URL']
except:
    warnings.warn('No database_url detected; please set it with config.', UserWarning)
try:
    email_user = os.environ['EMAIL_USER']
except:
    warnings.warn('No email_user detected; please set it with config.', UserWarning)
try:
    email_password = os.environ['EMAIL_PASS']
except:
    warnings.warn('No email_password detected; please set it with config.', UserWarning)
try:
    email_server = os.environ['EMAIL_SERVER']
except:
    warnings.warn('No email_server detected; please set it with config.', UserWarning)
