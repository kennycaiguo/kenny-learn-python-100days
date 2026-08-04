import scrapy
from scrapy import Selector,Request
from db_mv_crawler.items import MovieItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    # start_urls = ["https://movie.douban.com"]

    async def start(self):
        for page in range(10):
            yield Request(url=f"https://movie.douban.com/top250?start={page * 25}",callback=self.parse)
    
    def parse(self, response):
        sel = Selector(response)
        lis = sel.css('#content>div>div.article>ol>li')
        for li in lis:
            item = MovieItem()
            item['link'] = li.css('div.info>div.hd>a').attrib['href'] 
            item['title'] = li.css("div.info>div.hd>a>span:nth-child(1)::text").extract_first()
            item['rating'] = li.css("div.info>div.bd>div>span.rating_num::text").extract_first()
            item['subject'] = li.css('div.info>div.bd>p.quote>span::text').extract_first()

            yield item