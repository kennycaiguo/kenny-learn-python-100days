# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass

import scrapy


@dataclass
class DbMvCrawlerItem:
    # define the fields for your item here like:
    # name: str | None = None
    pass

class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name: str | None = None
    link = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    subject = scrapy.Field()
