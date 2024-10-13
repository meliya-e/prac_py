def superposition(funmod, funseq):
    funres = []
    for f in funseq:
        def fun(x, f = f):
            return funmod(f(x))
        funres.append(fun)
    return funres

