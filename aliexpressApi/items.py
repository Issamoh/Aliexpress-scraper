# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AliexpressapiItem(scrapy.Item):
    productName = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    storeName = scrapy.Field()
    productImageLink = scrapy.Field()

