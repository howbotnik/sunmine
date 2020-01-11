import requests
import ConfigController as Config

class Weather:
    api_url_base = "https://api.openweathermap.org/data/2.5/weather?q="
    built_url = ""

    def __init__(self):
        built_api_url = []
        built_api_url = self.addStringToUrlArray(built_api_url, self.api_url_base)
        built_api_url = self.addStringToUrlArray(built_api_url, Config.getLocation())
        built_api_url = self.addStringToUrlArray(built_api_url, ",")
        built_api_url = self.addStringToUrlArray(built_api_url, Config.getCountryCode())
        built_api_url = self.addStringToUrlArray(built_api_url, "&APPID=")
        built_api_url = self.addStringToUrlArray(built_api_url, Config.getOpenWeatherToken())
        self.built_url = self.convertArrayToString(built_api_url)

    def getWeatherData(self, url):
        r = requests.get(url)
        return r.json()

    def addStringToUrlArray(self, url_array, strToAdd):
        url_array.append(strToAdd)
        return url_array

    def convertArrayToString(self, array):
        return ''.join(array)