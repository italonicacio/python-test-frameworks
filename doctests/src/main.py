import doctest
from multiprocessing.sharedctypes import Value

def sum(v1: int, v2: int):
    """Return a sum of two numbers

    >>> sum(1, 1)
    2

    >>> sum(1, 2)
    3

    >>> sum(2, 1)
    3

    >>> sum('1', 1)
    Traceback (most recent call last):
        ...
    TypeError: v1 is not int!
    >>> sum(1, '1')
    Traceback (most recent call last):
        ...
    TypeError: v2 is not int!
    """

    if type(v1) is not int:
        raise TypeError("v1 is not int!")
    
    if type(v2) is not int:
        raise TypeError("v2 is not int!")

    return v1+v2


if __name__ == '__main__':
    doctest.testmod()
