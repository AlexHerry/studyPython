def trim(s):
    begin = None
    index = 0
    end = None
    length = len(s)
    while index < length:
        if begin is None and s[index] != ' ':
            begin = index
        if end is None and s[length-index-1] != ' ':
            end = length-index
        index = index + 1
    if begin is None and end is None:
        return ''
    return s[begin:end]


a = 'hello    '
print(len(a))
print(len(trim(a)))