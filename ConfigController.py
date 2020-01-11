import configparser
import ntpath
import json
import pathlib


class ConfigController:

    config = configparser.ConfigParser()
    config.read(pathlib.Path(__file__).parent / "sunmine.cfg")

    def __init__(self) -> None:
        super().__init__()

    def get_country_code(self):
        return self.config.get("Location", "country_code")

    def get_location(self):
        return self.config.get("Location", "location")

    def get_latitude(self):
        return self.config.get("Location", "latitude")

    def get_longitude(self):
        return self.config.get("Location", "longitude")

    def get_smtp_server(self):
        return self.config.get("Communication", "smtp_server_address")

    def get_smtp_port(self):
        return self.config.getint("Communication", "smtp_port")

    def get_sender_email(self):
        return self.config.get("Communication", "sender_email")

    def get_password(self):
        return self.config.get("Communication", "password")

    def get_recipient_email(self):
        return self.config.get("Communication", "recipient_email")

    def get_open_weather_token(self):
        return self.config.get("Tokens", "open_weather")

    def get_program_location(self):
        return self.config.get("Miner", "program_location")

    def get_program_name(self):
        path = self.config.get("Miner", "program_location")
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    def get_weather_codes(self):
        return json.loads(self.config.get("Weather_types", "weather_codes"))
