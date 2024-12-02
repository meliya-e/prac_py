with open("file2", "r") as f:
    data = f.read()
    dlin = len(data) // 3
while dlin < len(data) and data[dlin] != "\n":
    dlin += 1
print(data[:dlin])

