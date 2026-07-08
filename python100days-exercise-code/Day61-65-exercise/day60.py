"""
HTTPie：命令行HTTP客户端
安装 pip install httpie
使用，在一个cmd窗口里面输入: http --header https://m.douban.com/movie/

builtwith库：识别网站所用技术的工具
安装 pip install builtwith
使用:xx.py
import ssl

import builtwith

ssl._create_default_https_context = ssl._create_unverified_context
print(builtwith.parse('http://www.bootcss.com/'))
"""

def test1():
    import ssl
    import builtwith
    ssl._create_default_https_context = ssl._create_unverified_context
    print(builtwith.parse('http://www.bootcss.com/'))

def test2():
    import whois
    print(whois.whois('https://x.com/'))
    


if __name__ == '__main__':
    # test1()    
    test2()    