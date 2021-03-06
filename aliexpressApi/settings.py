# Scrapy settings for aliexpressApi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'aliexpressApi'

SPIDER_MODULES = ['aliexpressApi.spiders']
NEWSPIDER_MODULE = 'aliexpressApi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'aliexpressApi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
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
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'aliexpressApi.middlewares.AliexpressapiSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'aliexpressApi.middlewares.AliexpressapiDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'aliexpressApi.pipelines.AliexpressapiPipeline': 300,
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
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# PROXY_POOL_ENABLED = True
# ROTATING_PROXY_LIST = [
#     '148.72.156.56:3838',
#     '169.57.1.85:8123',
#     '169.57.1.84:80',
#     '163.172.230.102:3838',
#     '163.172.226.90:3838',
#     '163.172.228.245:3838',
#     '159.8.114.34:8123',
#     '195.154.47.113:3838',
#     '195.154.61.25:3838',
#     '167.86.96.193:80',
#     '161.35.220.7:80',
#     '51.254.98.24:80',
#     '173.192.128.238:9999',
#     '3.17.166.0:3838',
#     '199.102.46.199:3838',
#     '80.187.140.26:8080',
#     '199.102.46.215:3838',
#     '169.57.157.148:8123',
#     '51.89.4.140:8118',
#     '163.172.192.170:3838',
#     '82.119.170.106:8080',
#     '167.172.191.249:34584',
#     '80.48.119.28:8080',
#     '64.227.126.95:3128',
#     '52.17.193.191:80',
#     '192.162.244.145:3838',
#     '192.162.244.157:3838',
#     '169.57.157.146:8123',
#     '200.106.55.125:80',
#     '185.224.139.150:5218',
#     '163.172.60.116:8118',
#     '188.213.31.73:808',
#     '191.7.208.82:50626',
#     '159.224.44.19:33789',
#     '3.6.251.241:80',
#     '59.28.57.121:808',
#     '40.121.198.48:80',
#     '199.102.46.197:3838',
#     '39.137.69.7:80',
#     '175.212.226.51:80',
#     '39.137.69.6:8080',
#     '161.202.226.195:8123',
#     '78.189.14.221:8080',
#     '14.38.255.5:14143',
#     '221.180.170.104:8080',
#     '81.95.230.211:3128',
#     '161.202.226.194:8123',
#     '58.162.229.173:38893',
#     '185.162.142.81:53281',
#     '212.109.196.159:8118',
#     '201.33.227.221:57790',
#     '45.70.212.185:55443',
#     '188.165.141.114:3129',
#     '47.74.251.95:80'
#     '66.42.50.61:8118',
#     '166.159.90.56:53281',
#     '27.116.51.115:8080',
#     '178.33.251.230:3129',
#     '13.231.63.81:3838',
#     '175.44.42.4:3128',
#     '87.126.43.160:8080',
#     '145.239.121.218:3129',
#     '85.234.159.56:3838',
#     '193.242.177.105:53281',
#     '195.154.52.142:3838',
#     '51.254.237.77:3129',
#     '161.35.78.58:3128',
#     '199.102.46.210:3838',
#     '187.130.139.197:8080',
#     '14.38.255.25:80',
#     '182.52.51.10:37501',
#     '113.194.31.37:9999',
#     '37.152.176.247:8118',
#     '119.81.189.194:8123',
#     '159.8.114.37:25',
#     '160.19.244.139:48528',
#     '103.83.116.154:55443',
#     '94.127.144.179:43949',
#     '23.101.2.247:8118',
#     '41.162.52.11:8080',
#     '95.137.240.30:43188',
#     '103.216.51.210:8191',
#     '69.65.65.178:58389',
#     '175.44.42.195:3128',
#     '202.142.162.50:3128',
#     '85.90.215.111:3128',
#     '89.175.188.58:56263',
#     '198.245.53.173:9999',
#     '90.110.9.128:80',
#     '36.89.8.235:8080',
#     '124.90.51.224:8888',
#     '181.211.38.62:47911',
#     '195.154.252.205:3838',
#     '178.128.211.134:6868',
#     '41.160.40.2:37741',
#     '213.98.67.40:41005',
#     '91.207.147.243:38472',
#     '41.190.147.158:59912',
#     '181.112.40.114:49263',
#     '41.242.143.126:41632',
#     '212.200.246.24:80',
#     '110.74.219.189:34558',
#     '186.159.3.41:30334',
#     '123.56.118.36:8080',
#     '195.24.49.142:3128',
#     '186.42.124.130:65301',
#     '178.168.67.89:4645',
#     '41.84.131.78:53281',
#     '212.115.224.71:53281',
#     '177.37.240.52:8080',
#     '103.240.160.21:6666',
#     '62.152.75.110:50287',
#     '217.168.76.77:59021',
#     '1.20.97.181:55285',
#     '195.9.188.78:53281',
#     '3.16.50.235:3838',
#     '177.38.69.212:8080',
#     '46.8.28.17:8080',
#     '180.252.50.238:80',
#     '158.106.130.166:80',
#     '81.200.63.108:60579',
#     '91.203.36.102:55548',
#     '190.6.200.158:38256',
#     '46.99.255.235:8080',
#     '223.245.36.71:65309',
#     '117.54.4.245:30367',
#     '101.109.255.17:46085',
#     '103.216.82.209:54806',
#     '80.91.17.113:41258',
#     '103.3.225.114:36010',
#     '186.248.170.82:53281',
#     '82.149.203.178:8080',
#     '154.127.32.89:60020',
#     '157.119.207.35:8080',
#     '212.126.107.2:31475',
#     '46.219.80.142:30040',
#     '187.191.20.4:54375',
#     '5.58.85.32:53930',
#     '36.91.128.62:8902',
#     '85.237.46.168:45916',
#     '213.174.10.58:61855',
#     '51.255.103.170:3129',
#     '176.110.121.90:21776',
#     '5.160.14.130:54039',
#     '73.216.132.208:44428',
#     '89.23.198.13:8080',
#     '176.120.37.82:59365',
#     '61.135.155.82:443',
#     '103.83.116.218:55443',
#     '208.163.39.218:53281',
#     '94.205.254.82:3128',
#     '1.10.187.149:44976',
#     '94.141.244.39:34166',
#     '86.57.177.8:39303',
#     '211.137.52.159:8080',
#     '203.223.41.34:42104',
#     '186.235.83.186:44693',
#     '46.173.105.151:41258',
#     '78.8.45.68:8080',
#     '1.186.139.9:54754',
#     '46.150.76.25:56349',
#     '191.241.226.230:53281',
#     '191.7.208.81:50626',
#     '180.179.98.22:3128',
#     '91.187.113.205:53281',
#     '200.52.141.162:53281',
#     '118.174.232.239:39258',
#     '103.250.166.16:48340',
#     '95.79.99.148:3128',
#     '91.135.148.198:59384',
#     '204.15.243.233:58159',
#     '89.22.17.62:61616',
#     '181.40.84.38:49674',
#     '1.10.188.52:32163',
#     '118.70.12.171:53281',
# ]

ROTATING_PROXY_LIST_PATH = 'aliexpressApi/spiders/http_proxies.txt'
DOWNLOADER_MIDDLEWARES = {
    # ...
    # 'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    # 'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # 'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    # ...
}

