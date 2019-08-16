class Rabbit(object):
    def __init__(self, months):
        self._month_1 = 1
        self._adult = 0
        self._months = months

    def rab_count(self):
        for i in range(self._months - 1):
            self._month_1, self._adult = self._adult, self._month_1 + self._adult
        return self._month_1 + self._adult


if __name__ == '__main__':
    # month = int(input("一共几个月的兔子\n"))
    for i in range(1, 20):
        r = Rabbit(i)
        count = r.rab_count()
        print("一共有", count, "只兔子")