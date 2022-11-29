import time
from ..items import Listing
import scrapy
import re

from scrapy import Request

# documentation links : 
# source code :https://docs.scrapy.org/en/latest/_modules/scrapy/spiders/sitemap.html
# SitemapSpider : https://docs.scrapy.org/en/latest/topics/spiders.html
class DomainSpiderSpider(scrapy.spiders.SitemapSpider):
    LISTINGS_REGEX = r"https://www.domain.com.au/((\w+)(-\w+)*)$"
    BASE_DOMAIN = "domain.com.au"
    name = 'domain_spider'
    allowed_domains = ['domain.com.au']
    sitemap_urls = ['https://www.domain.com.au/sitemap-listings-sale-2022111004.xml','https://www.domain.com.au/sitemap-listings-rent-2022112404.xml','https://www.domain.com.au/new-homes-sitemap1.xml']

    sitemap_rules = [
        (re.compile(LISTINGS_REGEX), 'parse_listing_page'),
    ]

    def parse_listing_page(self,response):
        print(response.url)
        time.sleep(10)
        title = response.xpath(
            "//div[@class='css-1texeil']//text()".get().strip()
        )

        address = response.xpath (
            "//h1[@class='css-164r41r']//text()".get().strip()
        )

        # these 4 share the same xpath, 
        # to do : figure out how to differenciate them all 
        bedroom_count = response.xpath (
            "//span[@class='css-lvv8is']//text()".get().strip()
        )

        bathroom_count = response.xpath (
            "//h1[@class='css-164r41r']//text()".get().strip()
        )

        car_count = response.xpath (
            "//h1[@class='css-164r41r']//text()".get().strip()
        )

        unit_size = response.xpath (
            "//h1[@class='css-164r41r']//text()".get().strip()
        )

        # this share the same path as contact support's phone number
        unit_type = response.xpath(
            "//span[@class='css-in3yi3']"
        )

        # description attempt 1
        # this is a content container ?
        # unable to extract because it is not named, all containers share the same class 
        description = response.xpath(
            "//div[@class='noscript-expander-content css-1ij7r2s']"
        )

        # description attempt 2 
        # can get headline, but cant get the paragraphs,
        # as they are not named / classified 
        description_headline = response.xpath(
            "//h4[@data-testid='listing-details__description-headline']"
        )

        # description_paragraph = ?


        
        print(title,address)

        yield Listing(
            listing_title=title,
            listing_address=address
        )

