import asyncio
q1, q2 = asyncio.Queue(), asyncio.Queue()
async def put(name, value, queue, qname):
    await queue.put(value)
    print(f"{name}: put {value} to {qname}")

async def get(name, queue, qname):
    res = await queue.get()
    print("smth")
    return res

async def prod():
    for i in range(5):
        await put("prod", f"val_{i}", q1, "q1")
        await asyncio.sleep(1)
       # val = f"value_<{i}>"
       # res = await queue1.put(val)
      #  print(f"<{}>: put <{val}> to <{queue}>")

async def mid():
    while True:
        res = await get("mid", q1, "q1")
        await put("mid", res, q2, "q2")


async def cons():
    while True:
        await get("cons", q2, "q2")
        
async def main():
    tp, tm, tc = [asyncio.create_task(coro()) for coro in (prod, mid, cons)]
    await tp
    tm.cancel()
    tc.cancel()
