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
        self.fail()

    def test_get_latitude(self):
        self.fail()

    def test_get_longitude(self):
        self.fail()

    def test_get_smtp_server(self):
        self.fail()

    def test_get_smtp_port(self):
        self.fail()

    def test_get_sender_email(self):
        self.fail()

    def test_get_password(self):
        self.fail()

    def test_get_recipient_email(self):
        self.fail()

    def test_get_open_weather_token(self):
        self.fail()

    def test_get_program_location(self):
        self.fail()

    def test_get_program_name(self):
        self.fail()

    def test_get_weather_codes(self):
        self.fail()
