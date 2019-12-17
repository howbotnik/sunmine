import os
import getWeather
import getSunTimes
import timeCompare
import sendmail
import miningState
import psutil
import logging
import configController as config

def main():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.debug('Welcome to Sunmine 2019')

    currentState = miningState.getState()
    logging.debug("Current state of the miner: " + currentState)
																																																							   # weather
    logging.debug("Getting weather data from the internet...")
    weatherData = getWeather.getWeatherData()


    weatherId = weatherData.get("weather")[0].get("id")
    acceptableWeatherCodes = ["800", "801", "802"]

    # sunset/rise
    logging.debug("Getting sunrise/sunset data from the internet...")
    sunData = getSunTimes.getSunData()
    sunRise = sunData.get("results").get("sunrise")
    sunSet = sunData.get("results").get("sunset")

    goTime = False
    goTime = isTheSunUp(sunSet, sunRise)
    logging.debug("Sun is up: " + str(goTime))

    goWeather = False
    if goTime != False:
        for w in acceptableWeatherCodes:
            if w == str(weatherId):
                goWeather = True
                break
            else:
                goWeather = False
        logging.debug("Weather conditions: " + weatherData.get("weather")[0].get("main"))
        logging.debug("Weather is acceptable for mining: " + str(goWeather))

    output = ""
    if goTime == True and goWeather == True:
        logging.debug("Mining on")
        output = "Mining On"
        if isMinerAlreadyRunning(config.getProgramName()):
            logging.debug('Yes %s process was running, not starting.' % (config.getProgramName()))
        else:
            logging.debug('No process was running')
            os.startfile(config.getProgramLocation())
        if "off" in currentState:
            logging.debug("Changing state, sending email.")
            sendmail.send(output)
            miningState.setState("on")
    else:
        logging.debug("Mining Off")
        output = "Mining Off"
        if isMinerAlreadyRunning(config.getProgramName()):
            logging.debug('Yes %s process was running, killing.' % (config.getProgramName()))
            killProcess(config.getProgramName())

        else:
            logging.debug('Mining process not running, do not need to kill process.')
        if "on" in currentState:
            logging.debug("Changing state, sending email.")
            sendmail.send(output)
            miningState.setState("off")

def isMinerAlreadyRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def isTheSunUp(sunSet, sunRise):
    if timeCompare.isTimeInRange(sunSet, sunRise) == True:
        return True
    else:
        return False

def killProcess(processName):
    if os.name == "nt":
        # OS is windows
        os.system('Taskkill /IM ' + config.getProgramName())
    elif os.name == "posix":
        # OS is Linux
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == processName:
                proc.kill()


if __name__ == "__main__":
    main()
