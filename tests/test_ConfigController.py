from unittest import TestCase
from ConfigController import ConfigController


class TestConfigController(TestCase):

    def test_get_country_code(self):
        config = ConfigController()
        # check to see if returns type str
        self.assertIsInstance(config.get_country_code(), str)
        # check to see if returned value is 2 char long
        self.assertEqual(len(config.get_country_code()), 2)

    def test_get_location(self):
        config = ConfigController()
        self.assertIsInstance(config.get_location(), str)

    def test_get_latitude(self):
        config = ConfigController()
        self.assertIsInstance(config.get_latitude(), str)

    def test_get_longitude(self):
        config = ConfigController()
        self.assertIsInstance(config.get_longitude(), str)

    def test_get_smtp_server(self):
        config = ConfigController()
        self.assertIsInstance(config.get_smtp_server(), str)

    def test_get_smtp_port(self):
        config = ConfigController()
        self.assertIsInstance(config.get_smtp_port(), int)

    def test_get_sender_email(self):
        config = ConfigController()
        self.assertIsInstance(config.get_sender_email(), str)

    def test_get_password(self):
        config = ConfigController()
        self.assertIsInstance(config.get_password(), str)

    def test_get_recipient_email(self):
        config = ConfigController()
        self.assertIsInstance(config.get_recipient_email(), str)

    def test_get_open_weather_token(self):
        config = ConfigController()
        self.assertIsInstance(config.get_open_weather_token(), str)

    def test_get_program_location(self):
        config = ConfigController()
        self.assertIsInstance(config.get_program_location(), str)

    def test_get_program_name(self):
        config = ConfigController()
        self.assertIsInstance(config.get_program_name(), str)

    def test_get_weather_codes(self):
        config = ConfigController()
        self.assertIsInstance(config.get_weather_codes(), list)
