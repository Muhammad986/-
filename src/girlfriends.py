class Girlfriend:
    def __init__(self):
        self._happy = 100

    def level_1(self):
        self._happy -= 10
        return 20

    def level_2(self):
        self._happy -= 25
        return 40

    def level_3(self):
        self._happy -= 50
        return 60

    def level_4(self):
        self._happy -= 75
        return 80

    def happy_day(self):
        self._happy += 50
        return 10

    def _bad_day(self):
        if self._happy <= 0:
            return False
        else:
            raise