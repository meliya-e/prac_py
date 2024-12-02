with open("file", "rb") as f:
    data = f.read()
    part = int(len(data)/2)
with open("file", "wb") as f:
    res = data[part:] + data[:part]
    f.write(res)
