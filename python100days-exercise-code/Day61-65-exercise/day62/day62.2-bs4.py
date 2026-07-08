"""
使用bs4改写的获取豆瓣电影Top250电影名称的代码。
pip install beautifulsoup4 安装后叫做bs4
"""

def bs4_demo1():
    import bs4
    import requests
    
    file = open("dou_lns_bs4.txt",'w')
    for page in range(1, 11):
        resp = requests.get(
            url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
            headers={'User-Agent': 'BaiduSpider'}
        )
        # 创建BeautifulSoup对象
        soup = bs4.BeautifulSoup(resp.text, 'lxml')
        # 获取第二个a里面的链接
        alist = soup.select('div.info > div.hd > a')
        # print(alist)
        # 通过CSS选择器从页面中提取包含电影标题的span标签
        title_spans = soup.select('div.info > div.hd > a > span:nth-child(1)')
        # 通过CSS选择器从页面中提取包含电影评分的span标签
        rank_spans = soup.select('div.info > div.bd > div > span.rating_num')
        for title_span, rank_span,a in zip(title_spans, rank_spans,alist):
            print(title_span.text, rank_span.text)
            file.write(f"电影名称：{title_span.text}   评分：{rank_span.text} \n")
            print(a['href'])
            file.write(f'电影详情链接: {a["href"]}\n')
    file.close()        

if __name__ == '__main__':
    bs4_demo1()            