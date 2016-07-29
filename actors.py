import random

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print('The wizard {} attacks {}!'.format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print('Your roll is {}'.format(my_roll))
        print('{} rolls {}'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard has handily bested {}.'.format(creature.name))
            return True
        else:
            print('The wizard has been DEFEATED!')
            return False


class Creature:
    # level
    # name
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return "Creature {} of level {}".format(self.name, self.level)