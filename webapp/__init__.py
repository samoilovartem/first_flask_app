from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        page_title = 'Python News'
        news_list = get_python_news()
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'], 1)
        return render_template('index.html', page_title=page_title, weather=weather, news_list=news_list)

    return app
