import os
import sys
from Weather import Weather
from TimeCompare import TimeCompare
import SunTimes
import Sendmail
from MiningState import MiningState
import psutil
import logging
from ConfigController import ConfigController
import datetime

config = ConfigController()


def main():

    weather = Weather()
    acceptable_weather_codes = config.get_weather_codes()

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.debug('Welcome to Sunmine 2019')

    current_state = MiningState.get_state()
    logging.debug("Current state of the miner: " + current_state)																																																				   # weather

    # sunset/rise
    logging.debug("Getting sunrise/sunset data from the internet...")
    sun_api_url = SunTimes.build_sun_api_url(config)
    sun_data = SunTimes.get_sun_data_from_api(sun_api_url)
    sun_rise = sun_data.get("results").get("sunrise")
    sun_set = sun_data.get("results").get("sunset")

    go_time = False
    go_time = is_the_sun_up(sun_set, sun_rise)
    logging.debug("Sun is up: " + str(go_time))

    if not go_time:
        logging.debug("Sun is not up, program exiting.")
        sys.exit(0)

    logging.debug("Getting weather data from the internet...")
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
        logging.debug("Weather conditions: " + weather_data.get("weather")[0].get("main") + "- " + str(weather_id))
        logging.debug("Weather is acceptable for mining: " + str(go_weather))

    output = ""
    if go_time is True and go_weather is True:
        logging.debug("Mining on")
        output = "Mining On"
        if is_miner_already_running(config.get_program_name()):
            logging.debug('Yes %s process was running, not starting.' % (config.get_program_name()))
        else:
            logging.debug('No process was running')
            os.startfile(config.get_program_location())
        if "off" in current_state:
            logging.debug("Changing state, sending email.")
            Sendmail.send(output)
            MiningState.set_state("on")
    else:
        logging.debug("Mining Off")
        output = "Mining Off"
        if is_miner_already_running(config.get_program_name()):
            logging.debug('Yes %s process was running, killing.' % (config.get_program_name()))
            kill_process(config.get_program_name())

        else:
            logging.debug('Mining process not running, do not need to kill process.')
        if "on" in current_state:
            logging.debug("Changing state, sending email.")
            Sendmail.send(output)
            MiningState.set_state("off")


def is_miner_already_running(process_name):
    for process in psutil.process_iter():
        try:
            if process_name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
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
