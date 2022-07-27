# Python news Flask app

Originally this project was just my first flask app that displays collected in advance (parsed) Python news from [python.org](), but now the parsing process is automated (Celery) and the news source has been changed to [habr.com]() due to more interesting content. Also, there is a weather displaying based on API by [worldweatheronline.com]().

![alt text](https://miro.medium.com/max/1000/1*ZOq0qpYsOAy6a5dkv8s7Ew.jpeg)

### Installation 

1. Clone the repository from GitHub
2. Create a virtual environment
3. Install requirements: `pip install requirements.txt`
4. Create a file `config.py`
5. Fill it out:
```
import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = 'Your default city for weather API'
WEATHER_API_KEY = 'Your weather API key'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'Your secret key'
REMEMBER_COOKIE_DURATION = timedelta(days=5)
```
6. Go to sources root directory
7. Start the server: `./run.sh`



