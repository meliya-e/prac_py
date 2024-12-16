import asyncio

async def squarer(x):
    return x*x

async def doubler(x):
    return 2*x

async def main(x, y):
    async with asyncio.TaskGroup() as tg:
        a = tg.create_task(squarer(x))
        b = tg.create_task(squarer(y))
    async with asyncio.TaskGroup() as tg:
        e = tg.create_task(doubler(a.result()))
        f = tg.create_task(doubler(b.result()))
    return e.result(), f.result()
