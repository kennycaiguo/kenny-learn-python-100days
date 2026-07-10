def calc_average():
    total, counter = 0, 0
    avg_value = None
    while True:
        curr_value = yield avg_value
        total += curr_value
        counter += 1
        avg_value = total / counter


def main():
    obj = calc_average()
    # 生成器预激活
    obj.send(None)
    for _ in range(5):
        print(obj.send(float(input())))


import asyncio
import time


async def display(num):
    await asyncio.sleep(1)
    print(num)


def main2():
    start = time.time()
    objs = [asyncio.run(display(i)) for i in range(1, 10)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(objs))
    loop.close()
    end = time.time()
    print(f'{end - start:.3f}秒')

def main3():
    start = time.time()
    objs = [display(i) for i in range(1, 10)]
    future = asyncio.gather(*objs) 
    loop = asyncio.get_event_loop()
    future.add_done_callback(lambda x:print(x.result()))  
    loop.run_until_complete(future)
    loop.close()
    end = time.time()
    print(f'{end - start:.3f}秒')

if __name__ == '__main__':
    # main()
    # main2()
    main3()
    