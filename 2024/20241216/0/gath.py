import asyncio

async def squarer(x):
    return x*x

async def doubler(x):
    return 2*x

async def main(x, y):
        a, b = await asyncio.gather(squarer(x), squarer(y))
        return await asyncio.gather(doubler(a), doubler(b))
