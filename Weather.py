import requests
from ConfigController import ConfigController

class Weather:
    config = ConfigController()

    api_url_base = "https://api.openweathermap.org/data/2.5/weather?q="
    built_url = ""

    def __init__(self):
        built_api_url = []
        built_api_url = self.addStringToUrlArray(built_api_url, self.api_url_base)
        built_api_url = self.addStringToUrlArray(built_api_url, self.config.get_location())
        built_api_url = self.addStringToUrlArray(built_api_url, ",")
        built_api_url = self.addStringToUrlArray(built_api_url, self.config.get_country_code())
        built_api_url = self.addStringToUrlArray(built_api_url, "&APPID=")
        built_api_url = self.addStringToUrlArray(built_api_url, self.config.get_open_weather_token())
        self.built_url = self.convertArrayToString(built_api_url)

    def getWeatherData(self, url):
        r = requests.get(url)
        return r.json()

    def addStringToUrlArray(self, url_array, strToAdd):
        url_array.append(strToAdd)
        return url_array

    def convertArrayToString(self, array):
        return ''.join(array)