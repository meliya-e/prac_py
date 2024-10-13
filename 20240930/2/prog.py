lst = list(eval(input()))
size = len(lst)
for i in range(size):   
    for j in range( size-i - 1):
        key1 = (lst[j+1]**2) % 100
        key2 = (lst[j]**2) % 100
        if key2 > key1:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)

