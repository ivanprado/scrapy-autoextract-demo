import scrapy
from autoextract_poet.page_inputs import AutoExtractArticleData
from scrapy_poet import DummyResponse


class BlogZyteSpider(scrapy.Spider):
    name = 'blog_zyte'
    allowed_domains = ['zyte.com']
    start_urls = ['http://www.zyte.com/blog']

    def parse(self, response):
        post_links = response.css(".oxy-post-title")
        yield from response.follow_all(post_links, callback=self.parse_post)

    def parse_post(self, response: DummyResponse, article_data: AutoExtractArticleData):
        yield article_data.to_item()