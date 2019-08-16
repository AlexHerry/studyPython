import sys

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type for %s: \'%s\'' % (sys._getframe().f_code.co_name, type(x).__name__))
    if x >= 0:
        return x
    else:
        return -x

