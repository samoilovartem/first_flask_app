from datetime import datetime
import requests
from bs4 import BeautifulSoup
from webapp.model import db, News


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False


def get_python_news():
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').find_all('li')
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published_date = news.find('time').text
            try:
                published_date = datetime.strptime(published_date, '%b %d, %Y')
            except ValueError:
                published_date = datetime.now()
            save_news(title, url, published_date)


def save_news(title, url, published_date):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        news = News(title=title, url=url, published_date=published_date)
        db.session.add(news)
        db.session.commit()