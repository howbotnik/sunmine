import smtplib
from ConfigController import ConfigController
import sunmine_logger


class SendMail:
    logger = sunmine_logger.get_logger()

    def __init__(self):
        pass

    def send(self, message):
        self.logger.info("Sending email.")
        config = ConfigController()
        server = self.build_server(config)
        self.server_connect(server, config)
        self.server_ehlo(server)
        self.server_start_tls(server)
        self.server_ehlo(server)
        self.server_login(server, config)

        message = 'Subject: {}\n\n{}'.format(self.create_subject(message), self.create_email_body(message))

        self.send_mail(server, config, message)
        self.quit_server(server)

    def server_connect(self, server, config):
        # should return 220 (or in 200 range)
        return server.connect(config.get_smtp_server(), config.get_smtp_port())[0]

    def server_ehlo(self, server):
        # should return 250 (or in 200 range)
        return server.ehlo()[0]

    def server_start_tls(self, server):
        return server.starttls()[0]

    def create_subject(self, message):
        return "SUNMINE: " + message

    def create_email_body(self, message):
        return "Sunmine has set your mining rig to: " + message

    def build_server(self, config):
        return smtplib.SMTP(config.get_smtp_server(), config.get_smtp_port())

    def server_login(self, server, config):
        return server.login(config.get_sender_email(), config.get_password())[0]

    def send_mail(self, server, config, message):
        return server.sendmail(config.get_sender_email(), config.get_recipient_email(), message)

    def quit_server(self, server):
        return server.quit()[0]