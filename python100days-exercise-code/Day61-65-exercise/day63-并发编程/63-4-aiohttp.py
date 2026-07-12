"""
如果你需要使用异步爬虫，你不能使用requests，需要使用aiohttp库
安装： pip install aiohttp
"""
import asyncio
import re

import aiohttp
from aiohttp import ClientSession

TITLE_PATTERN = re.compile(r'<title.*?>(.*?)</title>', re.DOTALL)

async def fetch_page_title(url):
    async with ClientSession(
        headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    }) as session:
        async with session.get(url,ssl=False) as resp:
            if resp.status == 200:
                html = await resp.text()
                matcher = TITLE_PATTERN.search(html)
                title = matcher.group(1).strip()
                print(title)
def main():
    urls = [
        'https://www.python.org/',
        'https://www.jd.com/',
        'https://www.baidu.com/',
        'https://www.taobao.com/',
        'https://git-scm.com/',
        'https://www.sohu.com/',
        'https://gitee.com/',
        'https://www.amazon.com/',
        'https://www.usa.gov/',
        'https://www.nasa.gov/'
    ]

    jobs = [fetch_page_title(url) for url in urls]
    future = asyncio.gather(*jobs)
    loop = asyncio.get_event_loop()
    future.add_done_callback(lambda x:x)
    loop.run_until_complete(future)
    loop.close()


async def main2():
    urls = [
        'https://www.python.org/',
        'https://www.jd.com/',
        'https://www.baidu.com/',
        'https://www.taobao.com/',
        'https://git-scm.com/',
        'https://www.sohu.com/',
        'https://gitee.com/',
        'https://www.amazon.com/',
        'https://www.usa.gov/',
        'https://www.nasa.gov/'
    ]
    tasks = [asyncio.create_task(fetch_page_title(url)) for url in urls]
    await asyncio.wait(tasks)
   

if __name__ == '__main__':
    main()
    # asyncio.run(main2()) # 
    