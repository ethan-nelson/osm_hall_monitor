import smtplib
from osmhm import config

def basic_send_mail(to, subject, msg):
    import os
    program = '/usr/sbin/sendmail'
    email = os.popen("%s -t" % program, "w")
    email.write("From: %s\n" % config.email_user)
    email.write("Reply-to: %s\n" % config.email_user)
    email.write("To: %s\n" % to)
    email.write("Subject: %s\n" % subject)
    email.write("\n")
    email.write("%s\n" % msg)
    status = email.close()


def send_notification(notify_list, notification_type, notifier=basic_send_mail):
    SUBJECT = 'OSM Hall Monitor Notification |'
    messages = {}
    subjects = {}
    tos = {}

    for entry in notify_list:
        if entry['address'] is not '':
            if notification_type == 'user':
                MSG = """
Dear %s,
OSM Hall Monitor has detected an event for your consideration.

  **User alert**
       Time of event: %s
       Username: https://www.openstreetmap.org/user/%s
       Changeset: https://www.openstreetmap.org/changeset/%s
       Additions: %s
       Modifications: %s
       Deletions: %s
       Reason user is watched: %s

Problem? Feedback? Reply to this message.

Best,

OSM Hall Monitor
""" % (entry['author'], entry['timestamp'], entry['username'], entry['changesetid'], entry['create'], entry['modify'], entry['delete'], entry['reason'])

                TO = entry['address']
                NEWSUBJECT = '%s User %s ' % (SUBJECT, entry['username'])

            elif notification_type == 'object':
                if 'n' == entry['element'][0]:
                    pre = 'node'
                elif 'w' == entry['element'][0]:
                    pre = 'way'
                elif 'r' == entry['element'][0]:
                    pre = 'relation'
                if entry['action'] == 1:
                    act = 'create'
                elif entry['action'] == 2:
                    act = 'modify'
                elif entry['action'] == 4:
                    act = 'delete'
                MSG = """
Dear %s,
OSM Hall Monitor has detected an event for your consideration.

  **Object alert**
       Time of event: %s
       Object: https://www.openstreetmap.org/%s/%s
       Changeset: https://www.openstreetmap.org/changeset/%s
       Action: %s
       User performing: https://www.openstreetmap.org/user/%s
       Reason object is watched: %s

Problem? Feedback? Reply to this message.

Best,

OSM Hall Monitor
""" % (entry['author'], entry['timestamp'], pre, entry['element'][1:], entry['changesetid'], act, entry['username'], entry['reason'])

                TO = entry['address']
                NEWSUBJECT = '%s Object %s ' % (SUBJECT, entry['element'])
            else:
                print('Notification type unknown')
                continue
        else:
            continue

        addr = TO
        if addr not in tos:
            tos[addr] = TO
            subjects[addr] = NEWSUBJECT
            messages[addr] = MSG
        else:
            subjects[addr] = '%s: multiple events' % (SUBJECT)
            messages[addr] += '\r\n---NEXT ALERT---\r\n'+MSG

    for email in messages:
        try:
            notifier(tos[email], subjects[email], messages[email])
        except Exception as e:
            print('Issue sending notification: ', str(e))
            pass
