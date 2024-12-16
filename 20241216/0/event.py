import asyncio

async def snd(name, evsnd):
    evsnd.set()
    print("SND, <{name}>: generated <evsnd>")

async def mid(name, evsnd, evmid):
    await evsnd.wait()
    print("smth1")
    evmid.set()
    print("mid")

async def rcv(evmid1, evmid2):
    await evmid1.wait()
    print("smth2")
    await evmid2.wait()
    print("rcv")
    
async def main():
    evsnd, evmid0, evmid1 = asyncio.Event(), asyncio.Event(), asyncio.Event()
    await asyncio.gather(rcv(evmid0, evmid1), mid('123', evsnd, evmid1), mid('123', evsnd, evmid0), snd("456", evsnd))
    print("end")
