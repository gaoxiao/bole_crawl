# Scrapy settings for bole project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bole'

SPIDER_MODULES = ['bole.spiders']
NEWSPIDER_MODULE = 'bole.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'bole (+http://www.yourdomain.com)'


ITEM_PIPELINES = {
    'bole.pipelines.BolePipeline': 300
}

SPIDER_MIDDLEWARES = {
    'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 1,
}

LOG_LEVEL = 'INFO'
