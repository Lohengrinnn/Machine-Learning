#!/usr/bin/env python
# coding: utf-8

# In[7]:

import math

def isnum(val):
    """Return if an object is number.

    >>> [isnum(n) for n in [1, 1.2, "1.2", None]]
    [True, True, False, False]
    """
    return type(val) is int or type(val) is float

def mean(arr):
    """Return the mean of an array, expect non-number.
    >>> [mean(arr) for arr in [[1,2], [1,2,None]]]
    [1.5, 1.5]
    >>> mean([1,2,"String"])
    Traceback (most recent call last):
    ...
    TypeError
    """
    cum = 0.0
    cnt = 0.0
    for val in arr:
        if isnum(val):
            cum += val
            cnt += 1
        elif val:
            print("val %s type is %s", val, type(val))
            raise TypeError
    return cum / cnt

if __name__ == "__main__":
    import doctest
    doctest.testmod()