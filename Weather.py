import requests
from ConfigController import ConfigController


class Weather:
    config = ConfigController()

    api_url_base = "https://api.openweathermap.org/data/2.5/weather?q="
    built_url = ""

    def __init__(self):
        built_api_url = []
        built_api_url = self.add_string_to_url_array(built_api_url, self.api_url_base)
        built_api_url = self.add_string_to_url_array(built_api_url, self.config.get_location())
        built_api_url = self.add_string_to_url_array(built_api_url, ",")
        built_api_url = self.add_string_to_url_array(built_api_url, self.config.get_country_code())
        built_api_url = self.add_string_to_url_array(built_api_url, "&APPID=")
        built_api_url = self.add_string_to_url_array(built_api_url, self.config.get_open_weather_token())
        self.built_url = self.convert_array_to_string(built_api_url)

    def get_weather_data(self, url):
        r = requests.get(url)
        return r.json()

    def add_string_to_url_array(self, url_array, str_to_add):
        url_array.append(str_to_add)
        return url_array

    def convert_array_to_string(self, array):
        return ''.join(array)