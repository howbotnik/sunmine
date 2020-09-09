import os
from Weather import Weather
from TimeCompare import TimeCompare
import SunTimes
from SendMail import SendMail
from MiningState import MiningState
import psutil
import logging
from ConfigController import ConfigController
import sunmine_logger
import datetime

config = ConfigController()
send_mail = SendMail()

logger = sunmine_logger.get_logger()

def main():
    logger.info('Logging works!')

    weather = Weather()
    acceptable_weather_codes = config.get_weather_codes()

    logger.info('Started Sunmine application')

    current_state = MiningState.get_state()
    logger.info("Current state of the miner: " + current_state)																																																				   # weather

    # sunset/rise
    logger.info("Getting sunrise/sunset data from the internet...")
    sun_api_url = SunTimes.build_sun_api_url(config)
    sun_data = SunTimes.get_sun_data_from_api(sun_api_url)
    sun_rise = sun_data.get("results").get("sunrise")
    sun_set = sun_data.get("results").get("sunset")

    go_time = False
    go_time = is_the_sun_up(sun_set, sun_rise)
    logger.info("Sun is up: " + str(go_time))

    logger.info("Getting weather data from the internet...")
    weather_data = weather.get_weather_data(weather.built_url)

    weather_id = weather_data.get("weather")[0].get("id")

    go_weather = False
    if go_time:
        for w in acceptable_weather_codes:
            if w == str(weather_id):
                go_weather = True
                break
            else:
                go_weather = False
        logger.info("Weather conditions: " + weather_data.get("weather")[0].get("main") + " - " + str(weather_id))
        logger.info("Weather is acceptable for mining: " + str(go_weather))

    output = ""
    if go_time is True and go_weather is True:
        logger.info("Mining on")
        output = "Mining On"
        if is_miner_already_running(config.get_program_name()):
            logger.warning('Yes %s process was running, not starting.' % (config.get_program_name()))
        else:
            logger.warning('No process was running')
            os.startfile(config.get_program_location())
        if "off" in current_state:
            logger.warning("Changing state, sending email.")
            send_mail.send(output)
            MiningState.set_state("on")
    else:
        logger.info("Mining Off")
        output = "Mining Off"
        if is_miner_already_running(config.get_program_name()):
            logger.warning('Yes %s process was running, killing.' % (config.get_program_name()))
            kill_process(config.get_program_name())

        else:
            logger.warning('Mining process not running, do not need to kill process.')
        if "on" in current_state:
            logger.warning("Changing state, sending email.")
            send_mail.send(output)
            MiningState.set_state("off")


def is_miner_already_running(process_name):
    for process in psutil.process_iter():
        try:
            if process_name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            logger.critical('Psutil error, problem trying to access the process according to its name.')
            pass
    return False

def is_the_sun_up(sun_set, sun_rise):
    time_compare = TimeCompare(sun_set, sun_rise)
    if time_compare.is_time_in_range(time_compare.get_upper_time(), time_compare.get_lower_time(), datetime.datetime.now().time()):
        return True
    else:
        return False


def kill_process(process_name):
    if os.name == "nt":
        # OS is windows
        os.system('Taskkill /IM ' + config.get_program_name())
    elif os.name == "posix":
        # OS is Linux
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == process_name:
                proc.kill()



if __name__ == "__main__":
    main()
