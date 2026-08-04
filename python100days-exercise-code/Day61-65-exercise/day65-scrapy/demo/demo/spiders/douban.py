import scrapy
from scrapy import Selector,Request
from scrapy.http import HtmlResponse
from demo.items import MovieItem

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250?start=0&filter="]

    def parse(self, response:HtmlResponse):
        sel = Selector(response)
        lis=sel.css('#content > div > div.article > ol > li')
        for li in lis:
            item = MovieItem()
            item['link']    = li.css('div.info > div.hd > a').attrib['href']+'\t'
            item['title']   = li.css('div.info > div.hd > a > span:nth-child(1)::text').extract_first()+'\t'
            item['rating']  = li.css('div.info > div.bd > div > span.rating_num::text').extract_first()+'\t'
            item['subject'] = li.css("div.info > div.bd > p.quote > span::text").extract_first()
            yield item

        hrefs = sel.css('#content > div > div.article > div.paginator > a::attr("href")')    
        for href in hrefs:
            full_url = response.urljoin(href.extract())
            yield Request(url=full_url)