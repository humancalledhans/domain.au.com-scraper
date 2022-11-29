import scrapy


class DomainSpiderSpider(scrapy.spiders.SitemapSpider):
    LISTINGS_REGEX = r"https://apps.shopify.com/((\w+)(-\w+)*)$"

    BASE_DOMAIN = "domain.com.au"
    name = 'domain_spider'
    allowed_domains = ['domain.com.au']
    start_urls = ['http://domain.com.au/']

    def parse(self, response):
        pass
