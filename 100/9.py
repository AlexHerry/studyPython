import time


class TimeShow(object):
    __author__ = 'Alex'

    def __init__(self, *args):
        self._arg = args

    def prn_time(self):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(1)


