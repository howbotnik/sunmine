from unittest import TestCase
from Weather import Weather

class TestWeather(TestCase):
    def test_get_weather_data(self):
        self.fail()

    def test_add_string_to_url_array(self):
        array = []
        self.assertEqual(Weather.addStringToUrlArray(self, array, "firstString"), ["firstString"])
        self.assertEqual(Weather.addStringToUrlArray(self, array, "secondString"), ["firstString", "secondString"])

    def test_convert_array_to_string(self):
        array = ["I ", "like ", "making ", "unit ", "tests!"]
        self.assertEqual(Weather.convertArrayToString(self, array), "I like making unit tests!")
