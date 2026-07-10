from multiprocessing import Process,current_process
import time

def sub_task(content, nums):
    # 通过current_process函数获取当前进程对象
    # 通过进程对象的pid和name属性获取进程的ID号和名字
    print(f'PID: {current_process().pid}')
    print(f'Name: {current_process().name}')
    # 通过下面的输出不难发现，每个进程都有自己的nums列表，进程之间本就不共享内存
    # 在创建子进程时复制了父进程的数据结构，三个进程从列表中pop(0)得到的值都是20
    counter, total = 0, nums.pop(0)
    print(f'Loop count: {total}')
    time.sleep(0.5)
    while counter < total:
        counter += 1
        print(f'{counter}: {content}')
        time.sleep(0.01)


def main():
    nums = [20, 30, 40]
    # 创建并启动进程来执行指定的函数
    # Process(target=sub_task, args=('Ping', nums)).start()
    # Process(target=sub_task, args=('Pong', nums)).start()
    # p1 = Process(target=sub_task, args=('Ping', nums))

    for p in [ 
        Process(target=sub_task, args=('Ping', nums)),
        Process(target=sub_task, args=('Pong', nums)),
    ]:
        p.start()
    
    # 在主进程中执行sub_task函数
    sub_task('Good', nums)

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return n !=1    



def main2():
    import concurrent.futures

    PRIMES = [
        1116281,
        1297337,
        104395303,
        472882027,
        533000389,
        817504243,
        982451653,
        112272535095293,
        112582705942171,
        112272535095293,
        115280095190773,
        115797848077099,
        1099726899285419
    ] * 5    
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        primes = pool.map(is_prime,PRIMES)
        for num,prime in zip(PRIMES,primes):
            print(f'{num} is prime number?:{prime}')

# 进程间通讯
from multiprocessing import Process,Queue
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 50:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)

def main3():
    queue = Queue(0)  
    p1 = Process(target=sub_task,args=("ping",))
    p1.start()
    p2 = Process(target=sub_task,args=("pong",))
    p2.start()
    while p1.is_alive() and p2.is_alive():
        pass
    queue.put(50)

if __name__ == '__main__':
    # main()
    # main2()
    main3()



