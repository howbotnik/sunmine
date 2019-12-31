import configparser
import ntpath
import json

config = configparser.ConfigParser()
config.read("sunmine.cfg")

def getCountryCode():
    return config.get("Location", "country_code")

def getLocation():
    return config.get("Location", "location")

def getLatitude():
    return config.get("Location", "latitude")

def getLongitude():
    return config.get("Location", "longitude")

def getSMTPServer():
    return config.get("Communication", "smtp_server_address")

def getSMTPPort():
    return config.getint("Communication", "smtp_port")

def getSenderEmail():
    return config.get("Communication", "sender_email")

def getPassword():
    return config.get("Communication", "password")

def getRecipientEmail():
    return config.get("Communication", "recipient_email")

def getOpenWeatherToken():
    return config.get("Tokens", "open_weather")

def getProgramLocation():
    return config.get("Miner", "program_location")

def getProgramName():
    path = config.get("Miner", "program_location")
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def getWeatherCodes():
    return json.loads(config.get("Weather_types", "weather_codes"))
