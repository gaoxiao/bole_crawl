# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BoleItem(Item):
    title = Field()
    content = Field()
    pub_date = Field()
    info_area = Field()
    info_class = Field()
