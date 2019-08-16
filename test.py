# -*- coding:utf-8 -*-

import copy


will = ['hello', 123, 'world', [567, 'python']]
willer = copy.deepcopy(will)

print(id(will))
print(id(willer))
print('-----------------------1')

print([id(i) for i in will])
print([id(i) for i in willer])

print('-----------------------2')

print([i for i in will])
print([i for i in willer])

print('-----------------------3')

will[0] = 'qwe'
willer[3].append('New')

print([i for i in will])
print([i for i in willer])

print('-----------------------4')

print([i for i in will])
print([i for i in willer])

print('-----------------------5')

print([id(i) for i in will])
print([id(i) for i in willer])

print('-----------------------6')


s = {1,2}
s.add(1)
print(s)