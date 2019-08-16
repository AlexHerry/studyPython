# class Prime(object):
#     def __init__(self, specification):
#         self.__specification = specification
#         self.__L = [x for x in range(2, specification + 1)]
#
#     def prime(self):
#         for i in self.__L:
#             for j in range(2, self.__specification // i):
#                 if i*j in self.__L:
#                     self.__L.remove(i*j)
#         return self.__L
#


# class Prime(object):
#     def __init__(self, specification):
#         self.__specification = specification
#         self.__L = [x for x in range(2, specification + 1)]
#         self.__prime = []
#
#     def prime(self):
#         for i in self.__L:
#             for j in self.__L[0: i-1]:
#                 if i % j == 0:
#                     break
#             if j == i:
#                 self.__prime.append(i)
#         return self.__prime
#
#


class Prime(object):
    def __init__(self, small, big):
        self._specification = big
        self._small = small
        self._L = []

    def __sieve_of_eratosthenes(self):  # 埃拉托色尼筛选法，返回少于n的素数
        primes = [True] * (self._specification + 1)  # 范围0到n的列表
        p = 2  # 这是最小的素数
        while p * p <= self._specification:  # 一直筛到sqrt(n)就行了
            if primes[p]:  # 如果没被筛，一定是素数
                for i in range(p * 2, self._specification + 1, p):  # 筛掉它的倍数即可
                    primes[i] = False
            p += 1
        self._prime = [element for element in range(2, self._specification) if primes[element]]  # 得到所有少于n的素数
        return self._prime

    def run(self):
        self.__sieve_of_eratosthenes()
        for i in self._prime:
            if i > self._small:
                self._L.append(i)
        return self._L


# class Prime(object):
#     def __init__(self, specification):
#         self.__specification = specification
#         # self.__L = [x for x in range(2, specification + 1)]
#         self.__prime = []
#
#     def __odd_iter(self):
#         n = 1
#         while True:
#             n = n + 2
#             yield n
#
#     def __not_div(self, n):
#         return lambda x: x % n > 0
#
#     def __primes(self):
#         yield 2
#         it = self.__odd_iter()  # 初始序列
#         while True:
#             n = next(it)  # 返回序列的第一个数
#             yield n
#             it = filter(self.__not_div(n), it)  # 构造新序列
#
#     def main(self):
#         for n in self.__primes():
#             if n < self.__specification:
#                 self.__prime.append(n)
#             else:
#                 break
#         return self.__prime
#
#
if __name__ == '__main__':
    small = int(input('how small do you want'))
    big = int(input('how big do you want'))
    prime = Prime(small, big)
    print(prime.run())
