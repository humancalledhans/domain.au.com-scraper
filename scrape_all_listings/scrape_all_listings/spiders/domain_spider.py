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

    # only 3 of the urls are accessible, the other two links to compressed file (download required)
    # sitemap_urls = ['https://www.domain.com.au/sitemap-listings-sale-2022111004.xml','https://www.domain.com.au/sitemap-listings-rent-2022112404.xml','https://www.domain.com.au/new-homes-sitemap1.xml']
    sitemap_urls = ['https://www.domain.com.au/sitemap-listings-sale-2022111004.xml']

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

        # these 4 share the same xpath attributes - span[@class="css-lvv8is"]
        # The only difference between them is that they have different text in the next element 
        # therefore, [parent::] is used to differentiate them  
        # //span[contains(text(),"Beds")]//parent::span[@class="css-lvv8is"]        
        # #----------------------------------------------------------------
        
        # note: only works when there are NO other recommended properties on the page
        bedroom_count = response.xpath(
            "//span[contains(text(),'Beds')]//parent::span[@class='css-lvv8is']//text()".get().strip()
        )
        bathroom_count = response.xpath(
            "//span[contains(text(),'Baths')]//parent::span[@class='css-lvv8is']//text()".get().strip()
        )

        parking_count = response.xpath(
            "//span[contains(text(),'Parking')]//parent::span[@class='css-lvv8is']//text()".get().strip()
        )

        unit_size = response.xpath(
            "//span[@class='css-lvv8is' and contains(text(),'m²')]//text()".get().strip()
        )
        #----------------------------------------------------------------

        unit_type = response.xpath(
            "//div[@data-testid ='listing-summary-property-type']//span[@class='css-in3yi3']//text()".get().strip()
        )

        # description attempt 1
        # this is a content container ?
        # unable to extract because there are no other attributes to use 
        # all containers share the same class attribute
        #description = response.xpath(
        #    "//div[@class='noscript-expander-content css-1ij7r2s']"
        #)

        # description attempt 2 
        # can get headline, but cant get the paragraphs,
        # as they are not named / classified 
        description_headline = response.xpath(
            "//h4[@data-testid='listing-details__description-headline']"
        )

        full_description_list = response.xpath(
            # try using sibling ?
        )
        full_description = ""

        for sentence in full_description_list:
            if len(sentence) > 0:
                full_description = full_description + sentence

        print(title,address)

        yield Listing(
            listing_title=title,
            listing_address=address,
            listing_bedroom_count = bedroom_count,
            listing_bathroom_count = bathroom_count,
            listing_parking_count = parking_count,
            listing_unit_size = unit_size,
            listing_unit_type = unit_type,
            listing_full_description = full_description    
        )

