import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from recipe_crawler.items import RecipeCrawlerItem


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    allowed_domains = ["allrecipes.com"]
    start_urls = ["https://allrecipes.com/"]

    def parse(self, response):
        pass
