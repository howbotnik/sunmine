import requests
import configController as config

def getWeatherData():
    api_token = config.getOpenWeatherToken()
    location = config.getLocation()
    countryCode = config.getCountryCode()
    api_url_base = "https://api.openweathermap.org/data/2.5/weather?q="
    r = requests.get(api_url_base + location + "," + countryCode + "&APPID=" + api_token)
    return r.json()