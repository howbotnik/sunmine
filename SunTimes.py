import requests


def build_sun_api_url(config):
    lat = config.get_latitude()
    lng = config.get_longitude()
    return "https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng


def get_sun_data_from_api(api_url_base):
    r = requests.get(api_url_base)
    return r.json()
