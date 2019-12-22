import unittest
from Weather import Weather

class TestWeather(unittest.TestCase):
    weather = Weather()
    def test_addStringToUrl(self):
        self.assertEqual(self.weather.addStringToUrl("cheese", "cake"), "cheesecake")

if __name__ == '__main__':
    unittest.main()