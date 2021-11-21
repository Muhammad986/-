from src import player, casino, works, girlfriends


class Days:
    def __init__(self):
        self._point_player = player.Player()
        self._point_casino = casino.Casino()
        self._point_works = works.Works()
        self._point_girlfriends = girlfriends.Girlfriend()
        self._time = 24
        self._work_day = False

    def scroll(self):
        while True:
            def choice_works():
                if self._point_player.worker() == 1:
                    self._point_player.sleep -= 10
                    self._point_player.money += self._point_works.day_work()
                    self._work_day = True
                    print("Вы поработали!")
                else:
                    print("У вас нет работы, лох.")

            def choice_girlfriends():
                if self._point_player.sex():
                    self._point_player.sleep -= 10
                    print("1 - первый уровень. "
                          "2 - второй уровень. "
                          "3 - третий уровень. "
                          "4 - четвертый уровень. "
                          "5 - развлечь девушку. ")
                    choice_girlfriends_now = int(input("Что сделать с девушкой? "))
                    if choice_girlfriends_now == 1:
                        self._point_player.horny -= self._point_girlfriends.level_1()
                        print("Вы повесетились с девушкой на первом уровне!")
                    elif choice_girlfriends_now == 2:
                        self._point_player.horny -= self._point_girlfriends.level_2()
                        print("Вы повесетились с девушкой на втором уровне!")
                    elif choice_girlfriends_now == 3:
                        self._point_player.horny -= self._point_girlfriends.level_3()
                        print("Вы повесетились с девушкой на третьем уровне!")
                    elif choice_girlfriends_now == 4:
                        self._point_player.horny -= self._point_girlfriends.level_4()
                        print("Вы повесетились с девушкой на четвертом уровне!")
                    elif choice_girlfriends_now == 5:
                        self._point_player.money -= self._point_girlfriends.happy_day()
                        print("Вы провели с девушкой веселый день!")
                    else:
                        print("Вы ничего не сделали!")
                else:
                    print("У вас нет девушки, лох.")

            def choice_casino():
                self._point_player.sleep -= 10
                self._point_player.money += self._point_casino.play()
                print("Вы пошли в казино!")

            def choice_eater():
                if self._point_player.eater() == 0:
                    print("Вы умерли с голоду.")
                else:
                    print("Вы поели!")

            def choice_sleep():
                self._point_player.sleeper()
                print("Вы спите!")

            def end_day():
                if not self._work_day:
                    print("Вы не работа и получили пизды!")
                    self._point_works.day_not_work()
                    self._work_day = False
                else:
                    print("Вы работали и все прекрасно!")
                    self._work_day = False
                self._point_player.hungry -= 10
                self._point_player.thirst -= 10
                self._point_player.horny += 25
                self._point_player.sleeper()
                self.time = 24

            print("1 - работать. "
                  "2 - к девушке. "
                  "3 - казино. "
                  "4 - есть. "
                  "5 - спать. ")
            print(
                " Голод " + str(self._point_player.hungry) + "\n",
                "Жажда " + str(self._point_player.thirst) + "\n",
                "Деньги " + str(self._point_player.money) + "\n",
                "Сон " + str(self._point_player.sleep) + "\n",
                "Хорни " + str(self._point_player.horny) + "\n",
                "Работа " + str(self._point_player.work) + "\n",
                "Девушка " + str(self._point_player.girlfriend)
            )
            choice = int(input("Что сделать? "))
            if choice == 1:
                choice_works()
                self._time -= 8
            elif choice == 2:
                choice_girlfriends()
                self._time -= 2
            elif choice == 3:
                choice_casino()
                self._time -= 1
            elif choice == 4:
                choice_eater()
                self._time -= 1
            elif choice == 5:
                choice_sleep()
                self._time -= 6
            else:
                print("Вы ничего не сделали!")

            if self._time <= 0:
                end_day()