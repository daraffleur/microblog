from flask_mail import Message

from app import mail


def send_email(subject, sender, recepients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recepients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
