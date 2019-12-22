# sunmine

Sunmine is a piece of python software that aims to switch **on** your mining software during the most profitable **SOLAR** times. 
<br><br> 
It uses APIs that check if the sun has risen and the weather conditions in your specified location.
<br><br>

---

## Getting Started

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

## Built with
Python & PyCharm Community

---

## Authors
H. Wilson

---

## License

---

## Acknowledgements
#### Weather API provided by:
openweathermap.org

#### Sunrise / sunset data provided by:
api.sunrise-sunset.org
