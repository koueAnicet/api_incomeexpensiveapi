import email
from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subjet'],body=data['email_body'], to=data[data['to_email']]),
        email.send()