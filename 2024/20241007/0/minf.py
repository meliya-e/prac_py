def minf(*fun):
    def funk(x):
        return min([f(x) for f in fun]) 
    return funk
