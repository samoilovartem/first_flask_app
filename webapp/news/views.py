from webapp.weather import weather_by_city
from webapp.news.models import News
from flask import Blueprint, current_app, render_template


blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    page_title = 'Python News'
    news_list = News.query.order_by(News.published_date.desc()).all()
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'], 1)
    return render_template('news/index.html', page_title=page_title, weather=weather, news_list=news_list)

