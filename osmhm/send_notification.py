import smtplib
import config


def send_notification(notify_list, notification_type):
    def send_mail(FROM, TO, msg):
        server = smtplib.SMTP(SERVER, 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(config.email_user, config.email_password)
        server.sendmail(FROM, TO, msg)
        server.quit()

    SERVER = config.email_server

    FROM = config.email_user

    SUBJECT = 'OSM Hall Monitor Notification |'

    for entry in notify_list:
        if notification_type == 'user':
            if entry[5]:
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

                TO = [entry[5]]
                NEWSUBJECT = '%s User %s ' % (SUBJECT, entry[0][2])

                message = ("From: " + FROM,
                           "To: " + TO[0],
                           "Subject: " + NEWSUBJECT,
                           "", MSG)
                msg = '\r\n'.join(message)
                try:
                    send_mail(FROM, TO, msg)
                except:
                    pass

        elif notification_type == 'object':
            if entry[5]:
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

                TO = [entry[5]]
                NEWSUBJECT = '%s Object %s ' % (SUBJECT, entry[0][4])

                message = ("From: " + FROM,
                           "To: " + TO[0],
                           "Subject: " + NEWSUBJECT,
                           "", MSG)
                msg = '\r\n'.join(message)
                try:
                    send_mail(FROM, TO, msg)
                except:
                    pass
