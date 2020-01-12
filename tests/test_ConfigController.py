from unittest import TestCase
from ConfigController import ConfigController

class TestConfigController(TestCase):
    config = ConfigController()

    def test_get_country_code(self):
        # check to see if returns type str
        self.assertIsInstance(self.config.get_country_code(), str)
        # check to see if returned value is 2 char long
        self.assertEqual(len(self.config.get_country_code()), 2)

    def test_get_location(self):
        self.assertIsInstance(self.config.get_location(), str)

    def test_get_latitude(self):
        self.assertIsInstance(self.config.get_latitude(), str)

    def test_get_longitude(self):
        self.assertIsInstance(self.config.get_longitude(), str)

    def test_get_smtp_server(self):
        self.assertIsInstance(self.config.get_smtp_server(), str)

    def test_get_smtp_port(self):
        self.assertIsInstance(self.config.get_smtp_port(), int)

    def test_get_sender_email(self):
        self.assertIsInstance(self.config.get_sender_email(), str)

    def test_get_password(self):
        self.assertIsInstance(self.config.get_password(), str)

    def test_get_recipient_email(self):
        self.assertIsInstance(self.config.get_recipient_email(), str)

    def test_get_open_weather_token(self):
        self.assertIsInstance(self.config.get_open_weather_token(), str)

    def test_get_program_location(self):
        self.assertIsInstance(self.config.get_program_location(), str)

    def test_get_program_name(self):
        self.assertIsInstance(self.config.get_program_name(), str)

    def test_get_weather_codes(self):
        self.assertIsInstance(self.config.get_weather_codes(), list)
