class SimpleSort(object):
    __author__ = 'Alex'

    def __init__(self, lis=[]):
        self.__lis = lis
        # for i in args:
        #     self.__lis.append(i)

    def sort(self):
        for i in range(len(self.__lis)):
            for j in range(i, len(self.__lis)):
                if self.__lis[i] > self.__lis[j]:
                    self.__lis[i], self.__lis[j] = self.__lis[j], self.__lis[i]
        return self.__lis


if __name__ == '__main__':
    lis = []
    while True:
        num = input("输入数字(退出输入q)\n")
        if num == 'q':
            break
        lis.append(int(num))
    sort = SimpleSort(lis).sort()
    print(sort)