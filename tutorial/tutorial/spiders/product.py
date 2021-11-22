import scrapy
from ..items import Product
import datetime
import json
from scrapy.item import Item, Field
from scrapy_splash import SplashRequest

class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['allo.ua']
    start_urls = ['http://allo.ua/']


    def __init__(self, *args, **kwargs):
        self.hendled_items = set()
        super(ProductSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        parsed = response.xpath('//a[@class="sub__link arrow-icon"]/@href').getall()
        for url in parsed:
            yield SplashRequest(url=url, callback=self.parse_inside)


    def get_groups(self, response):
        return response.xpath('//a[@class="portal-group__image-link"]/@href').getall()


    def get_items(self, response):
        return response.xpath('//a[@class="product-card__title"]/@href').getall()

    def parse_inside(self, response):
        parsed = self.get_groups(response)
        parsed_items = self.get_items(response)
        if parsed:
            for href in parsed:
                yield response.follow(href, callback=self.parse_inside)
        elif parsed_items:
            for href in parsed_items:
                yield response.follow(href, callback=self.parse_item)
            next_page = response.xpath('//a[@class="pagination__next__link"]/@href').get()
            if not (next_page is None):
                yield response.follow(next_page, callback=self.parse_inside)



    def parse_item(self, response):

        item = Product()
        item['SKU'] = response.xpath('//span[@class ="p-tabs__sku-value"]/text()').get()
        if item['SKU'] in self.hendled_items:
            yield None

        item['time'] = datetime.datetime.now()
        item['title'] = response.xpath('//h1[@class ="p-view__header-title"]/text()').get()
        item['url'] = response.url
        item['category'] = response.xpath('//li/a[@class ="breadcrumbs__link"]/text()').getall()
        item['availability'] = bool(response.xpath('//span[@class ="p-trade__stock-label-icon"]').get())
        item['price'] = str(response.xpath('//div[contains(@class, "p-trade-price__current")]/span/text()')\
                                                                    .get()).encode("ascii","ignore").strip()
        item['price_regular'] = str(response.xpath('//div[@class ="p-trade-price__old"]/span[@class="sum"]/text()')\
                                                                        .get()).encode("ascii","ignore").strip()
        sel = response.xpath('//img[@class="shipping-brand__logo ls-is-cached lazyloaded"]').get()
        off = response.xpath('//span[@class ="product-discount-list__item-text-title"]').getall()
        print(sel)
        print(off)
        item['seller'] = sel
        item['offers'] = off
        self.hendled_items.add(item['SKU'])
        yield item
