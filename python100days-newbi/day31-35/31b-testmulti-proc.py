import threading
import glob
import os
from PIL import Image
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

PREFIX = 'thumbnails'

def gen_thumdnail(infile,size,format='png'):
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    file,ext = os.path.splitext(infile)
    file = file[file.rfind('/')+1:] # 获取纯文件名，去掉路径和扩展名
    # print(file)
    img = Image.open(infile)
    # print(img)
    img.thumbnail(size, Image.Resampling.LANCZOS)
    save_path = f'{PREFIX}/{file}_{size[0]}_{size[1]}{ext}'
    print(save_path)  
    img.save(save_path)  

def testProcessPool():
    with ProcessPoolExecutor() as excutor:
        if not os.path.exists(PREFIX):
            os.mkdir(PREFIX)  
        futures = []      
        for infile in glob.glob("./images/*.png"): # 大坑，用glob.glob变量的路径是./xxx\xxx.png的格式，需要统一路径，否则有问题
            infile = infile.replace('\\','/') # # ./images\cutesexy4.png，统一路径把 ./xxx\xxx.png变为./xxx/xxx.png
            for size in (16,32,48,64):
                result = excutor.submit(gen_thumdnail,infile,(size,size))
                futures.append(result)
    for f in futures:
        f.result()

if __name__ == '__main__':
    testProcessPool()
