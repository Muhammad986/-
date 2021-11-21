class Player:
    def __init__(self):
        self.money = 250
        self.hungry = 100
        self.thirst = 100
        self.sleep = 100
        self.horny = 0
        self.work = True
        self.girlfriend = True

    def eater(self):
        if self.money >= 25:
            self.hungry += 50
            self.thirst += 50
            self.money -= 25
        else:
            return 0

    def sleeper(self):
        self.sleep += 50

    def sex(self):
        if self.girlfriend:
            return 1
        else:
            return 0

    def worker(self):
        if self.work:
            return 1
        else:
            return 0