import shlex

s = input("FIO:")
m = input("mesto:")

#print(shlex.join(["register", s, m]))
res = shlex.join(["register", s, m])
print(res)
