import locale
import platform
from bs4 import BeautifulSoup

from webapp.db import db
from webapp.news.models import News

from datetime import datetime, timedelta

from webapp.news.parsers.utils import get_html, save_news


if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, 'Russian')
else:
    locale.setlocale(locale.LC_ALL, 'ru_Ru')


def parse_habr_date(date_str):
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    try:
        return datetime.strptime(date_str, '%d %B %Y в %H:%M')
    except ValueError:
        return datetime.now()


def get_news_snippets():
    html = get_html('https://habr.com/ru/search/?target_type=posts&q=python&order')
    habr_url = 'https://habr.com'
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find(
            'div', class_='tm-articles-list'
        ).find_all(
            'article', class_='tm-articles-list__item')
        for news in all_news:
            title = news.find('a', class_='tm-article-snippet__title-link').text
            url = habr_url + news.find('a', class_='tm-article-snippet__title-link')['href']
            published_date = news.find('span', class_='tm-article-snippet__datetime-published').text
            published_date = parse_habr_date(published_date)
            save_news(title, url, published_date)


def get_news_content():
    news_without_text = News.query.filter(News.text.is_(None))
    for news in news_without_text:
        html = get_html(news.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            news_text = soup.find('div', class_='tm-article-body').decode_contents()
            if news_text:
                news.text = news_text
                db.session.add(news)
                db.session.commit()

