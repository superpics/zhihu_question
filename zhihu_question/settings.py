# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_question project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu_question'

SPIDER_MODULES = ['zhihu_question.spiders']
NEWSPIDER_MODULE = 'zhihu_question.spiders'


DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu_question (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 随机延迟下载，0.5到1.5之间的一个随机值 * DOWNLOAD_DELAY 的结果作为等待间隔
RANDOM_DELAY = 2

# 对单个网站进行并发请求的最大值
#CONCURRENT_REQUESTS_PER_IP = 1

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
#    'zhihu_question.middlewares.ZhihuQuestionSpiderMiddleware': 543,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'zhihu_question.middlewares.ZhihuQuestionDownloaderMiddleware': 543,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihu_question.pipelines.ZhihuQuestionPipeline': 300,
   'zhihu_question.pipelines.SaveContentPipeline': 301,
   'zhihu_question.pipelines.ImgPipeline': 302
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 设置图片下载路径z
IMAGES_STORE = 'z:\\images\\'
# 图片过期天数，90天内抓取的都不会被重抓
IMAGES_EXPIRES = 90
# 该字段的值为XxxItem中定义的存储图片链接的image_urls字段
IMAGES_URLS_FIELD='image_urls'
# 该字段的值为XxxItem中定义的存储图片信息的images字段
IMAGES_RESULT_FIELD='images'
# 过滤小图片(可选)
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110
# 是否允许重定向(可选)
# MEDIA_ALLOW_REDIRECTS = True
# 生成缩略图(可选)
# IMAGES_THUMBS = {
#     'small': (50, 50),
#     'big': (270, 270),
# }