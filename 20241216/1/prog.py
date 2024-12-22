import asyncio

async def writer(queue, delay, stop_event, prefix):
    i = 0
    await asyncio.sleep(delay)
    while not stop_event.is_set():
        await queue.put((i, f"{i}_{prefix}"))
        i += 1
        await asyncio.sleep(delay)

async def stacker(queue, stack, stop_event):
    while not stop_event.is_set():
        try:
            item = await queue.get()
            await stack.put(item)
        except asyncio.CancelledError:
            break

async def reader(stack, count, delay, stop_event):
    await asyncio.sleep(delay)
    for _ in range(count):
        item = await stack.get()
        print(item[1]) # Выводим только строку, игнорируя счетчик
        await asyncio.sleep(delay)
    stop_event.set()

async def main(d1, d2, d3, count):
    queue = asyncio.Queue()
    stack = asyncio.Queue()
    stop_event = asyncio.Event()

    writer1 = asyncio.create_task(writer(queue, d1, stop_event, d1))
    writer2 = asyncio.create_task(writer(queue, d2, stop_event, d2))
    stacker_task = asyncio.create_task(stacker(queue, stack, stop_event))
    reader_task = asyncio.create_task(reader(stack, count, d3, stop_event))

    await reader_task

    writer1.cancel()
    writer2.cancel()
    stacker_task.cancel()

    try:
        await asyncio.gather(writer1, writer2, stacker_task)
    except asyncio.CancelledError:
        pass

d1, d2, d3, count = map(int, input().split(','))
asyncio.run(main(d1, d2, d3, count))
