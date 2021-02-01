import scrapy
from autoextract_poet.page_inputs import AutoExtractArticleData
from scrapy_poet import DummyResponse


class BlogScrapinghubSpider(scrapy.Spider):
    name = 'blog_scrapinghub'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):
        post_links = response.css(".more-link")
        yield from response.follow_all(post_links, callback=self.parse_post)

    def parse_post(self, response: DummyResponse, article_data: AutoExtractArticleData):
        yield article_data.to_item()