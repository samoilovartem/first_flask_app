from flask import Flask, render_template
from webapp.model import db, News
from webapp.weather import weather_by_city



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        page_title = 'Python News'
        news_list = News.query.order_by(News.published_date.desc()).all()
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'], 1)
        return render_template('index.html', page_title=page_title, weather=weather, news_list=news_list)

    return app
