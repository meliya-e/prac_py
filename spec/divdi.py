def divdigit(N):
    count = 0
    notchange = N
    while N > 0:
        n = N % 10    
        if n != 0 and notchange % n == 0:
            count += 1
        N //= 10
    return count
#    for i in str(N):
 #       n = int(i)    
  #      if N % n == 0 and n != 0:
   #         count += 1
