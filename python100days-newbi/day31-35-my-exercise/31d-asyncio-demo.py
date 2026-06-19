import asyncio

# 数字生成器函数
def num_generator(m,n):
    yield from range(m,n+1)

async def get_primer(m,n):
    primers = []
    for i in num_generator(m,n):
        is_primer = True
        for j in range(2,int(i**0.5+1)):
            if i % j == 0:
                is_primer = False
                break
        if is_primer:
            print("Primer Num:",i)
            primers.append(i)   
        await asyncio.sleep(0.001)
    return tuple(primers)    

async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares

def main():
    loop = asyncio.get_event_loop()
    future = asyncio.gather(get_primer(2,100),square_mapper(1,100))
    future.add_done_callback(lambda x:print(x.result()))
    loop.run_until_complete(future)
    loop.close()

if __name__ == '__main__':
    main()    