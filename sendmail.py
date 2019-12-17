import smtplib
import configController as config
import logging

def send(message):
    logging.debug("Sending email.")
    message = 'Subject: {}\n\n{}'.format(createSubject(message), createEmailBody(message))
    server = smtplib.SMTP(config.getSMTPServer(), 25)
    server.connect(config.getSMTPServer(), config.getSMTPPort())
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config.getSenderEmail(), config.getPassword())
    server.sendmail(config.getSenderEmail(), config.getRecipientEmail(), message)
    server.quit()

def createSubject(message):
    return "SUNMINE: " + message

def createEmailBody(message):
    return "Sunmine has set your mining rig to: " + message