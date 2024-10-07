def rbin(n, lst, b):
    if n > 1:
        rbin(n-1, lst + [b], 0)
        rbin(n-1, lst + [b], 1)
        return
    else:
        print(lst+[b])

        


