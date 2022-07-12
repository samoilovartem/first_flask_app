from celery import Celery
from celery.schedules import crontab

from webapp import create_app
from webapp.news.parsers import habr


flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def get_habr_snippets():
    with flask_app.app_context():
        habr.get_news_snippets()


@celery_app.task
def get_habr_content():
    with flask_app.app_context():
        habr.get_news_content()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), get_habr_snippets.s())
    sender.add_periodic_task(crontab(minute='*/2'), get_habr_content.s())