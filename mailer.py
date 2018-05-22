from flask import Flask
from flask_mail import Mail, Message

mailer = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.mail.yahoo.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'sarmatejas1006@yahoo.com',
    "MAIL_PASSWORD": 'neptunium93'
}

mailer.config.update(mail_settings)
mail = Mail(mailer)

if __name__ == '__main__':
    with mailer.app_context():
        msg = Message(subject="Web contact",
                      sender=mailer.config.get("MAIL_USERNAME"),
                      recipients=["sarmatejas1006@gmail.com"],  # replace with your email for testing
                      body="This is a test email I sent with Yahoo and Python!")
        mail.send(msg)
