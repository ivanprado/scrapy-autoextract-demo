# Scrapy settings for scrapy_autoextract_demo project

BOT_NAME = 'scrapy_autoextract_demo'

SPIDER_MODULES = ['scrapy_autoextract_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_autoextract_demo.spiders'

# Install AutoExtract provider
SCRAPY_POET_PROVIDERS = {"scrapy_autoextract.AutoExtractProvider": 500}

# Enable scrapy-poet's provider injection middleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy_poet.InjectionMiddleware': 543,
}

# Configure Twisted's reactor for asyncio support on Scrapy
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'