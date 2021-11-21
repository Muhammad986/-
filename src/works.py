class Works:
    def __init__(self):
        self._pay = 10
        self._level_work = 0
        self._deadline = 0

    def day_work(self):
        self._level_work += 1
        self._deadline = 0
        return self._pay

    def day_not_work(self):
        self._level_work -= 2
        self._deadline += 50

    def _gain_work(self):
        if self._level_work >= 5:
            self._pay = 20
        elif self._level_work >= 10:
            self._pay = 30
        elif self._level_work >= 15:
            self._pay = 40
        elif self._level_work >= 30:
            self._pay = 50
        else:
            raise

    def _bad_work(self):
        if self._deadline <= 100:
            return False
        else:
            raise