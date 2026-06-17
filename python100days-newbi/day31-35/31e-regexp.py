# import asyncio
# import re

# import aiohttp

# PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


# async def fetch_page(session, url):
#     async with session.get(url, ssl=False) as resp:
#         return await resp.text()


# async def show_title(url):
#     async with aiohttp.ClientSession() as session:
#         html = await fetch_page(session, url)
#         res = PATTERN.search(html).group('title')
#         print(res)
        


# def main():
#     urls = ('https://www.python.org/',
#             'https://git-scm.com/',
#             'https://www.jd.com/',
#             'https://www.taobao.com/',
#             'https://www.douban.com/')
#     loop = asyncio.get_event_loop()
#     cos = [asyncio.run(show_title(url)) for url in urls]
#     my_coroutine = asyncio.wait(cos)
#     future = asyncio.create_task(my_coroutine)
#     future.add_done_callback(lambda x :x.result())
#     loop.run_until_complete(future)
#     loop.close()
    


# if __name__ == '__main__':
#    main()

## not good