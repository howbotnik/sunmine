# sunmine

Sunmine is a piece of python software that aims to switch **on** your mining software during the most profitable **SOLAR** times. 
<br><br> 
It uses APIs that check if the sun has risen and the weather conditions in your specified location.
<br><br>

---

## Table of Contents

1. [Getting Started](#getting-started)<br>
    a. [Prerequisites](#prerequisites)<br>
    b. [Installing](#installing)<br>
    c. [Editing the config file](#editing-config)<br>
    d. [Running](#running)<br>
    e. [Setting up as a scheduled task](#setting-up-as-scheduled-task)<br>
2. [Built With](#built-with)
3. [Authors](#authors)
4. [The OpenWeatherMap API](#open-weather)
5. [Licence](#licence)


## Getting Started <a name="getting-started"></a>

### Prerequisites <a name="prerequisites"></a>
Your computer runs the following software:
* Python 3.7+ *[download](https://www.python.org/downloads/)*
* pip package installer *[download](https://pip.pypa.io/en/stable/installing/)*

### Installing <a name="installing"></a>

* `git clone https://github.com/howbotnik/sunmine.git`
* `cd sunmine`
* `pip install -r requirements.txt` 

#### Editing the config file (Essential) <a name="editing-config"></a>
* Open *sunmine.cfg*
* Read **CONFIG_README.md** for help setting up

### Running <a name="running"></a>
* `cd sunmine`
* `python main.py` <br/><br/>

#### Set up as a scheduled task: <a name="setting-up-as-a-scheduled-task"></a>
Use crontab or Windows 'Task Scheduler' if you want the program to run automatically.

---

## Built with <a name="built-with"></a>
Python & PyCharm Community <br>
Weather by https://Openweathermap.org <br>
Sun data by https://api.sunrise-sunset.org


---

## Authors <a name="authors"></a>
H. Wilson

---

## Open Weather API <a name="open-weather"></a>

The OpenWeatherMap API allows customization using the weather codes on this website:
* https://openweathermap.org/weather-conditions

As a default, sunmine is set up to use the following weather codes as acceptable for mining, but this may depend on your setup:
* 800 - Clear Sky 
* 801 - Few Clouds (11-25%)
* 802 - Scattered Clouds (25-50%)

Edit the acceptable weather codes in the config file for customization.


---

## Licence <a name="licence"></a>
MIT License

Copyright (c) 2020 Howard Wilson

