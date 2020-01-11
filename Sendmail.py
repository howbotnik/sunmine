import smtplib
from ConfigController import ConfigController
import logging


config = ConfigController()

def send(message):
    logging.debug("Sending email.")
    message = 'Subject: {}\n\n{}'.format(createSubject(message), createEmailBody(message))
    server = smtplib.SMTP(config.get_smtp_server(), 25)
    server.connect(config.get_smtp_server(), config.get_smtp_port())
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config.get_sender_email(), config.get_password())
    server.sendmail(config.get_sender_email(), config.get_recipient_email(), message)
    server.quit()

def createSubject(message):
    return "SUNMINE: " + message

def createEmailBody(message):
    return "Sunmine has set your mining rig to: " + message