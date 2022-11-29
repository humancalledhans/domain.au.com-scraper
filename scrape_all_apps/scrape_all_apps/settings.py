# Scrapy settings for scrape_all_apps project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrape_all_apps'

SPIDER_MODULES = ['scrape_all_apps.spiders']
NEWSPIDER_MODULE = 'scrape_all_apps.spiders'

# LOG_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrape_all_apps (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 99999999999999999

AUTOTHROTTLE_ENABLED = True

COOKIES_ENABLED = False

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 64
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrape_all_apps.middlewares.ScrapeAllAppsSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # this will use the 2,200 user agents from the scrapy_user_agents package.
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'webscrapingapi_scrapy_sdk.WebScrapingApiMiddleware': 543,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    # 'scrape_all_apps.smartproxy_auth.ProxyMiddleware': 100,
}

# SMARTPROXY_USER = 'sp69160830'
# SMARTPROXY_PASSWORD = 'Qwe123rty'
# SMARTPROXY_ENDPOINT = 'us.smartproxy.com'  # Endpoint you'd like to use
# SMARTPROXY_PORT = '10000'  # Port of the endpoint you are using.

# SMARTPROXY_USER = 'shopifyaso'  # Smartproxy Username (Sub-user)
# SMARTPROXY_PASSWORD = 'Qwe123rty'  # Password for your user
# SMARTPROXY_ENDPOINT = 'gate.dc.smartproxy.com'  # Endpoint you'd like to use
# SMARTPROXY_PORT = '20000'  # Port of the endpoint you are using.

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrape_all_apps.pipelines.ScrapeAllAppsPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 32.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 60 * 60 * 24 * 7
HTTPCACHE_DIR = 'httpcache'
CLOSESPIDER_PAGECOUNT = 32
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
