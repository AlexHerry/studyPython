def triangles():
    L = [1]
    yield L
    while True:
        L1 = L[:]
        L2 = L[:]
        L1.insert(0, 0)
        L2.append(0)
        for i in range(len(L1)):
            L1[i] = L1[i] + L2[i]
        L = L1
        yield L


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

