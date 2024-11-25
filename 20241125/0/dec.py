def dumper(fun):
     def newfun(*args, **kwargs):
         print(">", args, kwargs)
         res = fun(*args, *kwargs)
         print("<", res)
         return res
     return newfun

