# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
from demo.items import MovieItem

class DemoPipeline:
    def process_item(self, item):
        return item
    
class MovieItemPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = "豆瓣电影Top250"
        self.sheet.append(('名称', '评分', '名言'))

    def process_item(self, item:MovieItem,spider):
        self.sheet.append((item['title'],item['score'],item['motto']))
        return item   
    
    def close_spider(self,spider):
        self.wb.save("豆瓣电影top250.xlsx")
