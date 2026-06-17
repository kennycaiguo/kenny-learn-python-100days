import asyncio
import re

import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        res = PATTERN.search(html).group('title')
        return res
        

async def web_scrape():
      urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
      for url in urls:
          resp = await show_title(url)
          print(resp)

def main():
    loop = asyncio.get_event_loop()
    future = asyncio.gather(web_scrape())
    future.add_done_callback(lambda x :x.result())
    loop.run_until_complete(future)
    loop.close()
    


if __name__ == '__main__':
   main()