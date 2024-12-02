import pickle

class SerCls:
    lst = []
    dct = {}
    num = 0
    st = ""

ser = SerCls()
ser.lst = [1]
ser.dct["sec"] = 2
ser.num = 3
ser.st = "four"

res = pickle.dumps(ser)
print(res)
del ser
ser1 = pickle.loads(res)
print(ser1.lst)
print(ser1.dct)
print(ser1.st)
print(ser1.num)
