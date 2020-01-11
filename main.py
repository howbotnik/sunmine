import os
import sys
from Weather import Weather
from TimeCompare import TimeCompare
import SunTimes
import Sendmail
import MiningState
import psutil
import logging
from ConfigController import ConfigController
import datetime

def main():
    config = ConfigController()
    weather = Weather()
    acceptableWeatherCodes = config.get_weather_codes()

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.debug('Welcome to Sunmine 2019')

    currentState = MiningState.getState()
    logging.debug("Current state of the miner: " + currentState)																																																				   # weather


    # sunset/rise
    logging.debug("Getting sunrise/sunset data from the internet...")
    sunApiUrl = SunTimes.buildSunApiUrl(config)
    sunData = SunTimes.getSunDataFromApi(sunApiUrl)
    sunRise = sunData.get("results").get("sunrise")
    sunSet = sunData.get("results").get("sunset")

    goTime = False
    goTime = isTheSunUp(sunSet, sunRise)
    logging.debug("Sun is up: " + str(goTime))

    if goTime == False:
        sys.exit(0)

    logging.debug("Getting weather data from the internet...")
    weatherData = weather.getWeatherData(weather.built_url)

    weatherId = weatherData.get("weather")[0].get("id")

    goWeather = False
    if goTime != False:
        for w in acceptableWeatherCodes:
            if w == str(weatherId):
                goWeather = True
                break
            else:
                goWeather = False
        logging.debug("Weather conditions: " + weatherData.get("weather")[0].get("main") + "- " + str(weatherId))
        logging.debug("Weather is acceptable for mining: " + str(goWeather))

    output = ""
    if goTime == True and goWeather == True:
        logging.debug("Mining on")
        output = "Mining On"
        if isMinerAlreadyRunning(config.get_program_name()):
            logging.debug('Yes %s process was running, not starting.' % (config.get_program_name()))
        else:
            logging.debug('No process was running')
            os.startfile(config.get_program_location())
        if "off" in currentState:
            logging.debug("Changing state, sending email.")
            Sendmail.send(output)
            MiningState.setState("on")
    else:
        logging.debug("Mining Off")
        output = "Mining Off"
        if isMinerAlreadyRunning(config.get_program_name()):
            logging.debug('Yes %s process was running, killing.' % (config.get_program_name()))
            killProcess(config.get_program_name())

        else:
            logging.debug('Mining process not running, do not need to kill process.')
        if "on" in currentState:
            logging.debug("Changing state, sending email.")
            Sendmail.send(output)
            MiningState.setState("off")

def isMinerAlreadyRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def isTheSunUp(sunSet, sunRise):
    timeCompare = TimeCompare(sunSet, sunRise)
    if timeCompare.isTimeInRange(timeCompare.getUpperTime(), timeCompare.getLowerTime(), datetime.datetime.now()) == True:
        return True
    else:
        return False

def killProcess(processName):
    if os.name == "nt":
        # OS is windows
        os.system('Taskkill /IM ' + config.get_program_name())
    elif os.name == "posix":
        # OS is Linux
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == processName:
                proc.kill()


if __name__ == "__main__":
    main()
