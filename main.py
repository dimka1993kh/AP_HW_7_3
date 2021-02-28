from classes import WorkingWithMail
import time
from data import GMAIL_SMTP, GMAIL_IMAP, login, password, subject, recipients, message, header

if __name__ == '__main__':
    user = WorkingWithMail(mail_login=login, mail_password=password, SMTP=GMAIL_SMTP, )
    user.send(mail_message=message, email_to=recipients, message_subject=subject)
    time.sleep(10)
    user.recieve(IMAP=GMAIL_IMAP, header=header)