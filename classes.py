from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import imaplib
import email  

class WorkingWithMail():
    def __init__(self, mail_login, mail_password, SMTP):
        self.mail_login = mail_login
        self.mail_password = mail_password
        self.SMTP = SMTP
    def send(self, mail_message, email_to, message_subject):
        msg = MIMEMultipart()
        msg['From'] = self.mail_login
        msg['To'] = ', '.join(email_to)
        msg['Subject'] = message_subject
        msg.attach(MIMEText(mail_message))
        # Подключение
        connect = smtplib.SMTP(self.SMTP, 587)
        # identify ourselves to smtp gmail client
        connect.ehlo()
        # secure our email with tls encryption
        connect.starttls()
        # re-identify ourselves as an encrypted connection
        connect.ehlo()

        connect.login(self.mail_login, self.mail_password)
        connect.sendmail(self.mail_login, email_to, msg.as_string())
        connect.quit()

    def recieve(self, IMAP, header):
        mail = imaplib.IMAP4_SSL(IMAP)
        mail.login(self.mail_login, self.mail_password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        print('email_message', email_message)
        mail.logout()
