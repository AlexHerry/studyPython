class Daffodil(object):
    def __init__(self):
        self._L = []

    def num(self):
        for i in range(100, 1000):
            if int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3 == i:
                self._L.append(i)
        return self._L


if __name__ == '__main__':
   Daffodil = Daffodil()
   print(Daffodil.num())