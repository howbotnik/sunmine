import requests
import ConfigController as Config

class Weather:
    api_url_base = "https://api.openweathermap.org/data/2.5/weather?q="
    built_api_url = ""

    def __init__(self):
        self.built_api_url = self.buildUrl()

    def getWeatherData(self):
        r = requests.get(self.built_api_url)
        return r.json()

    def buildUrl(self):
        urlToBuild = ""
        urlToBuild = self.addStringToUrl(urlToBuild, self.api_url_base)
        urlToBuild = self.addStringToUrl(urlToBuild, Config.getLocation())
        urlToBuild = self.addStringToUrl(urlToBuild, ",")
        urlToBuild = self.addStringToUrl(urlToBuild, Config.getCountryCode())
        urlToBuild = self.addStringToUrl(urlToBuild, "&APPID=")
        urlToBuild = self.addStringToUrl(urlToBuild, Config.getOpenWeatherToken())
        return urlToBuild


    def addStringToUrl(self, strBuild, stringToAdd):
        strBuild += stringToAdd
        return strBuild
