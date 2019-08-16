class Multiplication(object):
    def __init__(self, num):
        self.__num = num + 1

    def prn(self):
        for i in range(1, self.__num):
            for j in range(1, i + 1):
                print("%3d * %d = %-5d" % (i, j, i * j), end='')
            print()


if __name__ == '__main__':
    num = int(input("你需要多大的乘法表\n"))
    Multiplication(num).prn()
