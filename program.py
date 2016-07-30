from actors import Wizard, Creature, SmallAnimal, Dragon
import random
import time

def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------------')
    print('                Wizard Game ')
    print('--------------------------------------')
    print('')



def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 84)
    # print(creatures)

    while True:

        active_creature = random.choice(creatures)
        print('A {} from level {} has appeared from a dark and steamy forest.'.format(active_creature.name, active_creature.level))
        print()
        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides to recuperate.')
                time.sleep(1)
                print('The wizard returns revitalized!')
        elif cmd == 'r':
            print('The wizard is unsure and flees.')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(
                    c.name, c.level
                ))
            print()
        else:
            print('OK, exiting game.')
            break
            
        if not creatures:
            print('You have defeated all!')
            break

if __name__ == '__main__':
    main()
