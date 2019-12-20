import requests
import ConfigController as Config

class Weather:
    api_url_base = "https://api.openweathermap.org/data/2.5/weather?q="
    built_api_url = ""

    def __init__(self):
        self.addStringToUrl(self.api_url_base)
        self.addStringToUrl(Config.getLocation())
        self.addStringToUrl(",")
        self.addStringToUrl(Config.getCountryCode())
        self.addStringToUrl("&APPID=")
        self.addStringToUrl(Config.getOpenWeatherToken())

    def getWeatherData(self):
        r = requests.get(self.built_api_url)
        return r.json()

    def addStringToUrl(self, stringToAdd):
        self.built_api_url += stringToAdd
