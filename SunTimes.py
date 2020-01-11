import requests

def buildSunApiUrl(config):
    lat = config.get_latitude()
    lng = config.get_longitude()
    return "https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng

def getSunDataFromApi(api_url_base):
    r = requests.get(api_url_base)
    return r.json()