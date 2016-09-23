import smtplib
import config

def send_mail(to, subject, msg):
    program = '/usr/sbin/sendmail'
    email = os.popen("%s -t" % program, "w")
    email.write("From: %s\n" % config.email_user)
    email.write("Reply-to: %s\n" % config.email_user)
    email.write("To: %s\n" % to)
    email.write("Subject: %s\n" % subject)
    email.write("\n")
    email.write("%s\n" % msg)
    status = email.close()


def send_notification(notify_list, notification_type, notifier=send_mail):
    SUBJECT = 'OSM Hall Monitor Notification |'
    messages = {}
    subjects = {}
    tos = {}

    for entry in notify_list:
        if notification_type == 'user':
            if entry[6]:
                MSG = """
Dear %s,
OSM Hall Monitor has detected an event for your consideration.

  **User alert**
       Time of event: %s
       Username: http://www.osm.org/user/%s
       Changeset: http://www.osm.org/changeset/%s
       Additions: %s
       Modifications: %s
       Deletions: %s
       Reason user is watched: %s

Problem? Feedback? Reply to this message.

Best,

OSM Hall Monitor
""" % (entry[4], entry[0][0], entry[0][2], entry[0][1], entry[0][3], entry[0][4], entry[0][5], entry[3])

                TO = entry[6]
                NEWSUBJECT = '%s User %s ' % (SUBJECT, entry[0][2])

        elif notification_type == 'object':
            if entry[6]:
                if 'n' == entry[0][4][0]:
                    pre = 'node'
                elif 'w' == entry[0][4][0]:
                    pre = 'way'
                elif 'r' == entry[0][4][0]:
                    pre = 'relation'
                MSG = """
Dear %s,
OSM Hall Monitor has detected an event for your consideration.

  **Object alert**
       Time of event: %s
       Object: http://www.osm.org/%s/%s
       Changeset: http://www.osm.org/changeset/%s
       Action: %s
       User performing: http://www.osm.org/user/%s
       Reason object is watched: %s

Problem? Feedback? Reply to this message.

Best,

OSM Hall Monitor
""" % (entry[4], entry[0][0], pre, entry[0][4][1:], entry[0][1], entry[0][3], entry[0][2], entry[3])

                TO = entry[6]
                NEWSUBJECT = '%s Object %s ' % (SUBJECT, entry[0][4])

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
        except Exception,e:
            print 'Issue sending notification: ', str(e)
            pass
