from functools import reduce


# 方法一:
# def str2float(s):
#     DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
#     index = s.index('.')
#     length = len(s) - index - 1
#     return reduce(lambda x, y: x*10+y, list(map(lambda s: DIGITS[s], s))[:index] + list(map(lambda s: DIGITS[s], s))[index+1:])/10**length


# 方法二:
# def str2float(s):
#
#     DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
#
#     def float_re(x, y):
#         if y == '.':
#             return x[0], 0.1
#         else:
#             return x[0]*10+y, x[1] if x[1] == 1 else x[1] * 0.1
#
#     z = reduce(float_re, [(0, 1)] + list(map(lambda x: DIGITS[x], s)))
#     return z[0]*10*z[1]
#
#
# print(str2float('123.456'))


# 方法3 （自己想的）:
from functools import reduce


def str2float(s):
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}

    def str_num(s):
        return dic[s]

    a = 0

    def float_str(x, y):
        nonlocal a
        if y == '.':
            a = 0
            return x
        else:
            a += 1
            return x * 10 + y

    return reduce(float_str, list(map(str_num, s))) / 10 ** a


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')