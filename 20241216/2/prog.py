import asyncio
from asyncio import Event
from math import log2
import random

async def merge(A1: list, A2: list, start, middle, finish, event_in1: Event, event_in2: Event, event_out: Event):
    if event_in1:
        await event_in1.wait()
    if event_in2:
        await event_in2.wait()
    i1, i2 = start, middle
    for i in range(start, finish):
        if i1 < middle and i2 < finish:
            if A1[i1] < A1[i2]:
                A2[i] = A1[i1]
                i1 += 1
            else:
                A2[i] = A1[i2]
                i2 += 1
        else:
            break
    i1 = i1 if i1 < middle else i2
    for i in range(i, finish):
        A2[i] = A1[i1]
        i1 += 1
    for i in range(start, finish):
        A1[i] = A2[i]
    event_out.set()

async def mtasks(Ain: list):
    n = len(Ain)
    if n <= 1:
        return [], Ain

    events = [None] * (n - 1)
    A = Ain.copy()
    B = [0] * n
    l = 1
    tasks = []
    while l < n:
        newevents = []
        num_tasks = n // (2 * l)
        for i in range(num_tasks):
            newevents.append(Event())
            start = 2 * i * l
            middle = (2 * i + 1) * l
            finish = min(2 * (i + 1) * l, n)
            event_in1 = events[2 * i] if 2 * i < len(events) else None
            event_in2 = events[2 * i + 1] if 2 * i + 1 < len(events) else None
            tasks.append(asyncio.create_task(merge(A, B, start, middle, finish, event_in1, event_in2, newevents[i])))

        if n % (2 * l) != 0:
            newevents.append(Event())
            start = num_tasks * 2 * l
            middle = start + l
            finish = n
            event_in1 = events[2 * num_tasks] if 2 * num_tasks < len(events) else None
            event_in2 = None
            tasks.append(asyncio.create_task(merge(A,B, start, middle, finish, event_in1, event_in2, newevents[-1])))

        await asyncio.gather(*tasks)
        events = newevents
        A, B = B, A
        l *= 2
    return tasks, A
import sys
exec(sys.stdin.read())
