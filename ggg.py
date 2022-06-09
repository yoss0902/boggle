
from functools import reduce
def count_appearances1(letter, word):

    fun = lambda a, c: c + 1 if a == letter
    # a, b = fun(0)

    return reduce(fun, word ,0)