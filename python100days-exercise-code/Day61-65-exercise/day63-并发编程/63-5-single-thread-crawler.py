"""
example04.py - 单线程版本爬虫
"""
import os
import requests
from pyquery import PyQuery as pq



def download_picture(url):
    filename = url[url.rfind('/') + 1:]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'images/beauty2/{filename}', 'wb') as file:
            file.write(resp.content)


def main():
   if not os.path.exists('images/beauty2'):
        os.makedirs('images/beauty2')
   doc = pq(filename='girls.txt')
   imgs = doc('.entity>span.img>img')
   for img in imgs:
       download_picture(img.attrib['src'])
    #   print(img.attrib['src'])

if __name__ == '__main__':
    main()