from datetime import datetime
from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

SPIDER_NAME = 'pep'
ALLOWED_DOMAINS = 'peps.python.org'
START_URLS = 'https://peps.python.org/'

TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
NOW_TIME = datetime.now().strftime(TIME_FORMAT)
FILE_NAME = f'status_summary_{NOW_TIME}.csv'

BASE_DIR = Path(__file__).parent.parent

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}
