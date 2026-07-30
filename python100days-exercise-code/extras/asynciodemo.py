import asyncio


async def display(num):
    await asyncio.sleep(1)
    print(num)

coroutines = [display(num) for num in range(10)]
future = asyncio.gather(*coroutines)
future.add_done_callback(lambda x:print(x.result()))
loop = asyncio.get_event_loop()
loop.run_until_complete(future)
loop.close()