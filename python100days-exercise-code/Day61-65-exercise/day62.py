"""
安装requests有坑，python3.11不要安装太高版本，会有警告，建议安装2.32.2
 pip install requests==2.32.2
"""
def crawler1():
    import requests
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    # res = requests.get("https://movie.douban.com/top250",headers=headers)
    # res = requests.get("https://news.sohu.com",headers=headers)
    res = requests.get("https://www.themoviedb.org/",headers=headers)
    if res.status_code == 200:
       print(res.content)
    #    print(res.text)
    #    with open('sohu.txt','w') as f:
       with open('movie.txt','wb') as f:
          f.write(res.content)

def crawler2():
   import re
   import requests

   headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
   pattern = re.compile(r'<a.*?href="(.*?)".*?title="(.*?)".*?>')
   resp = requests.get('https://sohu.com/',headers=headers)
   if resp.status_code == 200:
        all_matches = pattern.findall(resp.text)
        for href, title in all_matches:
            print(href)
            print(title)

def crawler3():
    import random
    import re
    import time

    import requests

    for page in range(1, 11):
        resp = requests.get(
            url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
            # 如果不设置HTTP请求头中的User-Agent，豆瓣会检测出不是浏览器而阻止我们的请求。
            # 通过get函数的headers参数设置User-Agent的值，具体的值可以在浏览器的开发者工具查看到。
            # 用爬虫访问大部分网站时，将爬虫伪装成来自浏览器的请求都是非常重要的一步。
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
        )
        # 通过正则表达式获取class属性为title且标签体不以&开头的span标签并用捕获组提取标签内容
        pattern1 = re.compile(r'<span class="title">([^&]*?)</span>')
        titles = pattern1.findall(resp.text)
        # 通过正则表达式获取class属性为rating_num的span标签并用捕获组提取标签内容
        pattern2 = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
        ranks = pattern2.findall(resp.text)
        # 使用zip压缩两个列表，循环遍历所有的电影标题和评分
        for title, rank in zip(titles, ranks):
            print(title, rank)
        # 随机休眠1-5秒，避免爬取页面过于频繁
        time.sleep(random.random() * 4 + 1)      


if __name__ == '__main__':
#    crawler1()
#    crawler2()
     crawler3()