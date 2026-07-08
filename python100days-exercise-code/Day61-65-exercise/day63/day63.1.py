"""
使用xpath来解析html页面，需要安装lxml
pip install lxml

"""
def lxml_demo1():
    from lxml import etree
    tree = etree.parse('books.xml')
    print(tree)
    root = tree.xpath("/bookstore")
    print(type(root))
    books = tree.findall("book")
    print(books)
    print(tree.xpath('//title[@lang]'))
    print(tree.findall('.//price'))

def lxml_get_douban():
    from lxml import etree
    import requests

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    file = open('doubanlink.txt','w')
    for page in range(1, 11):
        # print(page)
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}'
        print(url)
        resp = requests.get(
            url=url,
            headers=headers
        )
        tree = etree.HTML(resp.text)
        links = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[4]/div/div[2]/div[1]/a')
        # 通过XPath语法从页面中提取电影标题
        title_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
        # 通过XPath语法从页面中提取电影评分
        rank_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]')
       
        for title_span, rank_span,link in zip(title_spans, rank_spans,links):
            print(title_span.text, rank_span.text)   
            file.write(f"{title_span.text}:{rank_span.text}\n")
            file.write(f"link:{link.attrib['href']}\n") # 获取链接需要怎么写
    file.close()         

def lxml_get_douban2():
    from lxml import etree
    import requests

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    # file = open('doubanlink.txt','w')
    for page in range(1, 11):
        # print(page)
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}'
        resp = requests.get(
            url=url,
            headers=headers
        )
        tree = etree.HTML(resp.text)
        # links = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[4]/div/div[2]/div[1]/a')
        # # 通过XPath语法从页面中提取电影标题
        # title_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]')
        # # 通过XPath语法从页面中提取电影评分
        # rank_spans = tree.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]')
       
        # for title_span, rank_span,link in zip(title_spans, rank_spans,links):
        #     print(title_span.text, rank_span.text)   
        #     file.write(f"{title_span.text}:{rank_span.text}\n")
        #     file.write(f"link:{link.attrib['href']}\n") # 获取链接需要怎么写
        for i in range(1,26):
            li = tree.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{i}]')
            link = li.find("//a")
            print(link.attrib['href'])

    # file.close()  

def get_all_page_links():
    from lxml import etree
    import requests
    file = open("dou_links.txt","w")
    for page in range(1, 11):
        # print(page)
        url=f'https://movie.douban.com/top250?start={(page - 1) * 25}'
        get_links(url,file)
        print("===============================")
    file.close()

def get_links(url,file):
    from lxml import etree
    import requests

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    # url=f'https://movie.douban.com/top250?start=0'
    print(f"working on : {url}")
    resp = requests.get(url=url,headers=headers)
    tree = etree.HTML(resp.text)
    lis = tree.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for l in lis:
        links = l.xpath(".//div/div[2]/div[1]/a")
        for link in links:
            print(link.attrib['href'])
            file.write(link.attrib['href']+'\n')



if __name__ == '__main__':
    # lxml_demo1()
    # lxml_get_douban()
    # get_links()
    get_all_page_links();