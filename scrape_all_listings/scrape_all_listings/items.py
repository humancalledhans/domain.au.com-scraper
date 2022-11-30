# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class ScrapeAllListingsItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class Listing(scrapy.Item):
    listing_title = scrapy.Field
    listing_address = scrapy.Field
    listing_bedroom_count = scrapy.Field
    listing_bathroom_count = scrapy.Field
    listing_parking_count = scrapy.Field
    listing_unit_size = scrapy.Field
    listing_unit_type = scrapy.Field
    listing_full_description = scrapy.Field