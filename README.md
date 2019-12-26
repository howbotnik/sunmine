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
    d. [Running](#runnning)<br>
    e. [Setting up as a scheduled task](#setting-up-as-scheduled-task)<br>
2. [Built With](#built-with)
3. [Authors](#authors)
4. [Licence](#licence)
5. [Acknowledgements](#acknowledgements)


## Getting Started <a name="getting-started"></a>

### Prerequisites
Your computer runs the following software:
* Python 3.7+ *[download](https://www.python.org/downloads/)*
* pip package installer *[download](https://pip.pypa.io/en/stable/installing/)*

### Installing

* `git clone https://github.com/howbotnik/sunmine.git`
* `cd sunmine`
* `pip install -r requirements.txt` 

#### Editing the config file (Essential)
* Open *sunmine.cfg*
* Read **CONFIG_README.md** for help setting up

### Running
* `cd sunmine`
* `python main.py` <br/><br/>

#### Set up as a scheduled task:
Use crontab or Windows 'Task Scheduler' if you want the program to run automatically.

---

## Built with <a name="built-with"></a>
Python & PyCharm Community <br>
Weather by Openweathermap.org <br>
Sun data by api.sunrise-sunset.org


---

## Authors <a name="authors"></a>
H. Wilson

---

## Licence <a name="licence"></a>

---

## Acknowledgements <a name="acknowledgements"></a>

