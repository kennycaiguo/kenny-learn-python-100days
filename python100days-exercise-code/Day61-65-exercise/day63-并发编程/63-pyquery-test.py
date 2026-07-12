from pyquery import PyQuery as pq

doc = pq(filename='girls.txt')
imgs = doc('.entity>span.img>img')
for img in imgs:
    print(img.attrib['src'])