class Days(object):
    def __init__(self, year, month, days):
        self.__year = year
        self.__month = month
        self.__day = days
        self.__leap_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __leap_year(self):
        if self.__year % 400 == 0:
            return True
        elif self.__year % 4 == 0 and self.__year % 100 != 0:
            return True
        else:
            return False

    def __detection(self):
        if self.__month > 12:
            return "输入正确的月份"
        if self.__day > self.__leap_months[self.__month-1]:
            if self.__leap_year() and self.__month == 2 and self.__day <= 29:
                return None
            return "输入正确的天数"

    def date(self):
        if self.__detection() is not None:
            return self.__detection()
        num = self.__day
        for i in range(self.__month-1):
            num += self.__leap_months[i]
        if self.__leap_year() and month > 2:
            num += 1
            return num
        else:
            return num


if __name__ == '__main__':
    year = int(input("请输入年份"))
    month = int(input("请输入月份"))
    day = int(input("请输入天数"))
    date = Days(year, month, day).date()
    print(date)
