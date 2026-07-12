# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from dataclasses import dataclass


@dataclass
class DemoItem:
    # define the fields for your item here like:
    # name: str | None = None
    pass

class MovieItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    motto = scrapy.Field()


