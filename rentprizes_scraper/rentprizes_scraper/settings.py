# Scrapy settings for rentprizes_scraper project

BOT_NAME = 'rentprizes_scraper'
SPIDER_MODULES = ['rentprizes_scraper.spiders']
NEWSPIDER_MODULE = 'rentprizes_scraper.spiders'
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2
USER_AGENT = 'Opera/8.72 (Windows NT 5.1; sl-SI) Presto/2.11.320 Version/11.00'
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'
