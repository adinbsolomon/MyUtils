
def listify(*args):
    l = []
    for arg in args:
        l += arg if type(arg)==list else [arg]
    return l
def tuplify(*args):
    t = ()
    for arg in args:
        t = t + (arg if type(arg)==tuple else (arg,))
    return t
