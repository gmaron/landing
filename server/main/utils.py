import re
from email.mime.text import MIMEText
import smtplib
import os

# Define a function for 
# for validating an Email 
def check(email):
    # Make a regular expression 
    # for validating an Email 
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    # pass the regualar expression 
    # and the string in search() method 
    if (re.search(regex, email)):
        return True

    return False


def send_email(name, mail, message):
    username = os.getenv("GMAIL_MAIL")

    msg = MIMEText(message)
    msg['Subject'] = 'New message from {}. Mail: {}'.format(name, mail)
    msg['From'] = username
    msg['To'] = username
    msg = msg.as_string()

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(username, os.getenv("GMAIL_APP_PASS"))
    session.sendmail(username, username, msg)
    session.quit()

    return True
