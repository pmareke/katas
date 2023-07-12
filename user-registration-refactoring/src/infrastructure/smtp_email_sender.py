import smtplib
import ssl

from src.domain.email_sender import EmailSender


class SmtpEmailSender(EmailSender):
    def __init__(self, password: str = "myPassword") -> None:
        self.password = password

    def send(self, from_email: str, to_email: str, subject: str) -> None:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login("my@gmail.com", "myPassword")
            server.sendmail(from_email, to_email, subject)
