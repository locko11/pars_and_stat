import scrapy
from ..items import Product
import datetime
import json
from scrapy.item import Item, Field
from inline_requests import inline_requests
from ..settings import OFFERS_REQUEST_HEADER

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
            yield response.follow(url=url, callback=self.parse_inside)


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

    @inline_requests
    def parse_item(self, response):
        item = Product()
        item['SKU'] = response.xpath('//span[@class ="p-tabs__sku-value"]/text()').get()
        if item['SKU'] in self.hendled_items:
            yield None

        try:
            url = f"https://allo.ua/ua/discounts/product/items/?sku={item['SKU']}&isAjax=1&currentLocale=uk_UA"
            resp = yield scrapy.http.Request(url, headers=OFFERS_REQUEST_HEADER)
            item['offers'] = sorted([i['text'] for i in json.loads(resp.text)])
        except Exception:
            self.logger.info(f"Failed request {url}", exc_info=True)

        item['time'] = datetime.datetime.now()
        item['title'] = response.xpath('//h1[@class ="p-view__header-title"]/text()').get()
        item['url'] = response.url
        item['category'] = response.xpath('//li/a[@class ="breadcrumbs__link"]/text()').getall()
        item['availability'] = bool(response.xpath('//span[@class ="p-trade__stock-label-icon"]').get())
        item['price'] = str(response.xpath('//div[contains(@class, "p-trade-price__current")]/span/text()')\
                                                                    .get()).encode("ascii","ignore").strip()
        item['price_regular'] = str(response.xpath('//div[@class ="p-trade-price__old"]/span[@class="sum"]/text()')\
                                                                         .get()).encode("ascii","ignore").strip()
        item['seller']= response.xpath('//span[@class="shipping-brand__name"]/text()').get() or 'ALLO'
        # item['seller'] = response.xpath('//div[@class="shipping-seller__brand shipping-brand"]/img/@src').get()
        self.hendled_items.add(item['SKU'])
        yield item
