import asyncio
from time import time


async def print_nums():  # replaces @asyncio.coroutine
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)  # replaces yield from


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f"{count} seconds have passed")
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())  # replaces ensure_future()
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())  # replaces 3 lines above
