from webapp.weather import weather_by_city
from webapp.news.models import News
from flask import abort, Blueprint, current_app, render_template


blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    page_title = 'Python News'
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.published_date.desc()).all()
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'], 1)
    return render_template('news/index.html', page_title=page_title, weather=weather, news_list=news_list)


@blueprint.route('/news/<int:news_id>')
def show_single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()
    if not my_news:
        abort(404)
    return render_template('news/single_news.html', page_title=my_news.title, news=my_news)