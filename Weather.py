import requests
import ConfigController as Config

class Weather:
    api_url_base = "https://api.openweathermap.org/data/2.5/weather?q="
    built_api_url = ""

    def __init__(self):
        self.addApiUrlBaseToBuiltUrl()
        self.addLocationToBuiltUrl()
        self.addCommaToBuiltUrl()
        self.addCountryCodeToBuiltUrl()
        self.addAppIdToBuiltUrl()
        self.addApiTokenToBuiltUrl()

    def getWeatherData(self):
        r = requests.get(self.built_api_url)
        print("App url" + self.built_api_url)
        return r.json()

    def addApiUrlBaseToBuiltUrl(self):
        self.built_api_url += self.api_url_base

    def addCommaToBuiltUrl(self):
        self.built_api_url += ","

    def addCountryCodeToBuiltUrl(self):
        self.built_api_url += Config.getCountryCode()

    def addAppIdToBuiltUrl(self):
        self.built_api_url += "&APPID="

    def addApiTokenToBuiltUrl(self):
        self.built_api_url += Config.getOpenWeatherToken()

    def addLocationToBuiltUrl(self):
        self.built_api_url += Config.getLocation()