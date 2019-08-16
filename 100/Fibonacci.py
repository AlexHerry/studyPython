class Fibonacci(object):
    def __init__(self, count):
        self.__count = count
        self.__lis = []

    def __fib(self, count_num):
        return 1 if count_num<= 2 else self.__fib(count_num-1) + self.__fib(count_num-2)

    def cyc(self):
        for i in range(1, self.__count + 1):
            self.__lis.append(self.__fib(i))
        return self.__lis


if __name__ == '__main__':
    num = int(input("需要多少个斐波那契数列的数\n"))
    lis = Fibonacci(num).cyc()
    print(lis)