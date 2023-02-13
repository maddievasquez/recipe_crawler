# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecipeCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    ingredients = scrapy.Field()
    directions = scrapy.Field()
    recipeLink = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
