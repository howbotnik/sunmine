import requests
import configController as config

def getSunData():
    lat = config.getLatitude()
    lng = config.getLongitude()
    api_url_base = "https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng
    r = requests.get(api_url_base)
    return r.json()