import sys


# Sequential map

def sequential_map(*args) -> list:
    args = [*args]
    cont = args.pop()
    for fun in args:
        cont = list(map(fun, cont))
    return cont


# Consensus filter

def consensus_filter(*args) -> list:
    args = [*args]
    cont = args.pop()
    for fun in args:
        cont = list(filter(fun, cont))
    return cont


# Conditional reduce

def conditional_reduce(fun_1, fun_2, cont) -> int:
    filt_cont = iter(filter(fun_1, cont))
    val = next(filt_cont)
    for el in filt_cont:
        val = fun_2(val, el)
    return val


# Functional chain

def func_chain(*functions):
    funcs = [*functions][::-1]

    def composite_function(*args):
        arguments = list(args)
        while funcs:
            arguments = list(map(funcs.pop(), arguments))
        match len(arguments):
            case 1:
                return (lambda x: x)(*arguments)
            case _:
                return arguments

    return composite_function


## Integration to the first task

def sequential_map_func(*args):
    args = [*args]
    cont = args.pop()
    function = func_chain(*args)
    return function(*cont)


# Multiple partial

def single_partial(func, /, *args, **kwargs):
    def newfunc(*fargs, **fkwargs):
        newkwargs = {**kwargs, **fkwargs}
        return func(*args, *fargs, **newkwargs)

    return newfunc


def multiple_partial(*args, **kwargs):
    return [single_partial(arg, **kwargs) for arg in args]


# Print function

def my_print(*texts, sep='', end='\n', file=sys.stdout):
    text = list(map(str, texts))
    out = sep.join(text)
    file.write(f'{out}{end}')
