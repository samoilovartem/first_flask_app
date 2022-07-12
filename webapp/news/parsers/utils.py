import requests

from webapp.db import db
from webapp.news.models import News


def get_html(url):
    headers = {
        "User-Agent": "Mozilla / 5.0 (Macintosh; Intel MacOS X 10.15; rv:102.0) "
                      "Gecko/20100101 Firefox/102.0"
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False


def save_news(title, url, published_date):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        news = News(title=title, url=url, published_date=published_date)
        db.session.add(news)
        db.session.commit()

