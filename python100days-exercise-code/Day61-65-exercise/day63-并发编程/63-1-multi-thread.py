import random
import time
from threading import Thread

def download(*,filename):
    start = time.time()
    print(f"开始下载{filename}")
    time.sleep(random.randint(3,6))
    print(f"{filename}下载完成")
    wait = time.time() - start
    print(f"下载一共耗时{wait: .3f}秒")

def main():
    start = time.time()
    download(filename='Python从入门到住院.pdf')
    download(filename='MySQL从删库到跑路.avi')
    download(filename='Linux从精通到放弃.mp4')
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')

def main2():
    # 定义线程列表
    threads = [
        Thread(target=download,kwargs={"filename":"Python从入门到住院.pdf"}),
        Thread(target=download,kwargs={"filename":"MySQL从删库到跑路.avi"}),
        Thread(target=download,kwargs={"filename":"Linux从精通到放弃.mp4"}),
    ]
    start = time.time()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()    
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')

# 使用Thread的子类，可以把需要执行的任务放到run方法里面
class DownloadThread(Thread):
    def __init__(self, filename):
        self.filename = filename
        super().__init__()   

    def run(self):
        start = time.time()
        print(f"开始下载{self.filename}")
        time.sleep(random.randint(3,6))
        print(f"{self.filename}下载完成")
        wait = time.time() - start
        print(f"下载一共耗时{wait: .3f}秒")     

def main3():
    threads = [
        DownloadThread('Python从入门到住院.pdf'),
        DownloadThread('MySQL从删库到跑路.avi'),
        DownloadThread('Linux从精通到放弃.mp4'),
    ]
    start = time.time()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()    
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')

#ThreadPoolExecutor
def main4():
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as pool:
         filenames = ['Python从入门到住院.pdf', 'MySQL从删库到跑路.avi', 'Linux从精通到放弃.mp4']
         start = time.time()
         for file in filenames:
             pool.submit(download,filename = file)
    duration = time.time() - start
    print(f'总耗时: {duration:.3f}秒.')


"""
所谓“守护线程”就是在主线程结束的时候，不值得再保留的执行线程。这里的不值得保留指的是守护线程会在其他非守护线程全部运行结束之后被销毁，
它守护的是当前进程内所有的非守护线程。简单的说，守护线程会跟随主线程一起挂掉，而主线程的生命周期就是一个进程的生命周期。如果不理解，
我们可以看一段简单的代码。
"""

def display(content):
    while True:
        print(content, end='', flush=True)
        time.sleep(0.1)


def main5():
    Thread(target=display, args=('Ping', ), daemon=True).start() #如果这里没有daemon=True就是死循环，不会结束
    Thread(target=display, args=('Pong', ), daemon=True).start() #如果这里没有daemon=True就是死循环，不会结束
    time.sleep(5) # 主线程结束，即使守护线程里面的是死循环，它也会将其中断，然后守护线程退出，程序结束

# 如何有效的避免多线程程序中的资源竞争问题
from concurrent.futures import ThreadPoolExecutor
from threading import RLock

class Account(object):
    def __init__(self):
        self.balance = 0.0
        self.lock = RLock()

    def deposite(self,value):
       self.lock.acquire()
       try:
        newVal = self.balance + value
        time.sleep(0.01) 
        self.balance = newVal
       finally:
           self.lock.release()

def main6():
    acc = Account()
   
    with ThreadPoolExecutor(max_workers=16) as pool:
        for _ in range(100):
            pool.submit(acc.deposite,1)
    print(acc.balance)

if __name__ == '__main__':
    # main()     # 总耗时: 14.005秒.
    # main2()      # 总耗时: 6.002秒.
    # main3()
    # main4()
    # main5()
    main6()