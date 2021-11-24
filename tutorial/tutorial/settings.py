# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# from shutil import which
#
#
# SELENIUM_DRIVER_NAME = 'chrome'
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
# SELENIUM_DRIVER_ARGUMENTS=['--headless']

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# SPLASH_URL = 'http://localhost:8050'

FEED_EXPORT_ENCODING= "utf-8"
FEED_EXPORT_FIELDS = ['time', 'title', 'url', 'SKU', 'category', 'availability', 'price', 'price_regular', 'seller', 'offers']
FEED_FORMAT="csv" # формат файла для вывода данных(json, csv, xml)
FEED_URI="data.csv" # путь для сохранения файла
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.33
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',

}
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
    # 'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
    # 'scrapy_splash.SplashCookiesMiddleware': 723,
    # 'scrapy_splash.SplashMiddleware': 725,
    # 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    # 'scrapy_selenium.SeleniumMiddleware': 800,
}


# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#     'scrapy.extensions.telnet.TelnetConsole': None,
#     'scrapy_selenium.SeleniumMiddleware': 800,
# }
# LOG_ENABLED = False
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


OFFERS_REQUEST_HEADER = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,pl;q=0.5,de;q=0.4",
    "content-type": "text/plain",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "x-use-nuxt": "1",
    "cookie": "store=default_ua; sc=A560FF21-D703-AA5F-AB3C-4E8C1C35FA61; _ga=GA1.2.1106823896.1609335498; fp=16; lfp=12/30/2020, 3:38:19 PM; _userGUID=0:kjbgszn7:UzMxUlydfLVPeQV2BQypSWxDQFMk4n1d; pa=1609335500735.47310.1702135271956413allo.ua0.5769418185731663+1; city_id=4; __uzma=e25377de-e4c7-45dc-89b5-9b7e3134e1c4; __uzmb=1637676791; __uzme=5839; frontend=77d3a3248bb64bb68da676af7798e913; is_bot=0; __ssds=2; _gcl_au=1.1.1812205655.1637676794; __utmc=45757819; __utmz=45757819.1637676794.2.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __ssuzjsr2=a9be0cd8e; __uzmaj2=d76dc550-7dd1-4fd0-93f3-644fbec887e4; __uzmbj2=1637676791; _gid=GA1.2.1414909773.1637676795; __exponea_etc__=83241073-5653-49af-963f-4d7f5e6e760b; _hjid=818c9711-2471-47bc-86d0-d2873c44ee4a; _hjSessionUser_54409=eyJpZCI6Ijk5MzA1ZTNmLTE2MDctNTA0Ni05YjQwLWVlZTE0MjJjNGNkYiIsImNyZWF0ZWQiOjE2Mzc2NzY3OTU1MjYsImV4aXN0aW5nIjp0cnVlfQ==; frontend_hash=oWqS3Q77d3a3248bb64bb68da676af7798e913aKq3rv; store=default_ua; protocol=https; abTestAllo=group2; __utma=45757819.1106823896.1609335498.1637684032.1637748873.4; __exponea_time2__=-0.06634378433227539; __insp_wid=1964961402; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly9hbGxvLnVhLw%3D%3D; __insp_targlpt=0IbQvdGC0LXRgNC90LXRgiDQvNCw0LPQsNC30LjQvSDQvNC_0LHRltC70YzQvdC40YUg0YLQtdC70LXRhNC_0L3RltCyLCDQvdC_0YPRgtCx0YPQutGW0LIsINGC0LXQu9C10LLRltC30L7RgNGW0LIsINGE0L7RgtC_0LDQv9Cw0YDQsNGC0ZbQsiwg0LLRltC00LXQvtC60LDQvNC10YAsINC%2F0L7QsdGD0YLQvtCy0L7RlyDRgtC10YXQvdGW0LrQuC4g0JTQvtGB0YLQsNCy0LrQsCDQsiDQmtC40ZfQsiwg0JTQvdGW0L%2FRgNC_0L%2FQtdGC0YDQvtCy0YHRjNC6LCDQpdCw0YDQutGW0LIsINCU0L7QvdC10YbRjNC6LCDQntC00LXRgdCwLCDQv9C_INCj0LrRgNCw0ZfQvdGWIOKAkyDRltC90YLQtdGA0L3QtdGCLdC80LDQs9Cw0LfQuNC9IEFMTE8udWEh; _hjSession_54409=eyJpZCI6ImMxOWZmODkzLTc1ODUtNGU2Mi04MjQ5LTc4MTJiNGYwMzViMyIsImNyZWF0ZWQiOjE2Mzc3NDg4NzQ2Mzd9; _hjIncludedInSessionSample=1; _hjAbsoluteSessionInProgress=0; __insp_norec_sess=true; dSesn=c673f0b0-05a7-6075-3d0c-047988089d19; _dvs=0:kwdde7yc:Uos4TwTHKhnoSzokbFaE75E8XWZXBZvJ; detect_mobile_type=2; __utmt=1; __utmb=45757819.7.9.1637748885435; __uzmcj2=815317317059; __uzmdj2=1637749606; _dc_gtm_UA-63509214-1=1; _dc_gtm_UA-63509214-3=1; _gat=1; __insp_slim=1637749610200; private_content_version=808ffd2a4e32ef43e3eb611847d8f3fa; t_s_c_f_l=0%3A2%3A506545afd2e57668%3AVGl2%2FOiuxxPjwu2HWUlFOA%3D%3D; _gat_UA-63509214-1=1; id1185517833-smartbanner-closed=true; __uzmc=6443130723716; __uzmd=1637749619",
    "Referer": "https://allo.ua/ua/products/mobile/xiaomi-11t-8-128gb-meteorite-gray.html",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }
