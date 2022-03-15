import scrapy
import json
from scrapy.utils.response import open_in_browser
from ..items import AliexpressapiItem


class AliexpressSpider(scrapy.Spider):
    name = 'aliexpress'
    def start_requests(self):
        headers = {
            "accept" : "application/json, text/plain, */*",
            "accept-encoding" : "gzip, deflate, br",
            "accept-language" : "en-GB,en;q=0.9",
            "cache-control" : "no-cache",
            "pragma" : "no-cache",
            "referer" : "https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=smartphones&ltype=wholesale&SortType=default&page=1",
            "sec-ch-ua" : '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
            "sec-ch-ua-mobile" : "?0",
            "sec-ch-ua-platform" : '"Windows"',
            "sec-fetch-dest" : "empty",
            "sec-fetch-mode" : "cors",
            "sec-fetch-site" : "same-origin",
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        }
        url = 'https://www.aliexpress.com/glosearch/api/product?trafficChannel=main&d=y&CatId=0&SearchText=smartphones&ltype=wholesale&SortType=default&page=2&origin=y'

        req = scrapy.Request(url=url,headers=headers)
        yield req

    def parse(self, response):
        data = json.loads(response.body)

        products = data['mods']['itemList']['content']
        item = AliexpressapiItem()
        for product in products:
            item['productName'] = product['title']['displayTitle']
            item['price'] = product['prices']['salePrice']['formattedPrice']
            if(product.get('evaluation',None) is None):
                item['rating'] = 'None'
            else:
                item['rating'] = product['evaluation']['starRating']
            item['storeName'] = product['store']['storeName']
            item['productImageLink'] = product['image']['imgUrl']
            yield item
