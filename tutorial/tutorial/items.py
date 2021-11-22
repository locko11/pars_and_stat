# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    # define the fields for your item here like:
    time = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    SKU = scrapy.Field()
    category = scrapy.Field()
    availability = scrapy.Field()
    price = scrapy.Field()
    price_regular = scrapy.Field()
    seller = scrapy.Field()
    offers = scrapy.Field()
