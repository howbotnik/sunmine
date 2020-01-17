from unittest import TestCase
from Weather import Weather
from ConfigController import ConfigController


class TestWeather(TestCase):
    def test_get_weather_data(self):
        config = ConfigController()
        apiTokenFromConfig = config.get_open_weather_token()
        testApiUrl = "https://api.openweathermap.org/data/2.5/weather?q=London,GB&APPID=" + apiTokenFromConfig
        data = Weather.get_weather_data(testApiUrl)
        assert 'weather' in data
        assert 'main' in data
        assert 'wind' in data
        assert 'clouds' in data
        assert 'sys' in data
        assert 'coord' in data


    def test_add_string_to_url_array(self):
        array = []
        self.assertEqual(Weather.add_string_to_url_array(self, array, "firstString"), ["firstString"])
        self.assertEqual(Weather.add_string_to_url_array(self, array, "secondString"), ["firstString", "secondString"])

    def test_convert_array_to_string(self):
        array = ["I ", "like ", "making ", "unit ", "tests!"]
        self.assertEqual(Weather.convert_array_to_string(self, array), "I like making unit tests!")
