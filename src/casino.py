import random


class Casino:
    def play(self):
        jack_pot = random.randint(0, 100)
        if jack_pot > 75:
            
            return 250
        else:

            return 0