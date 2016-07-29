from actors import Wizard, Creature
import random

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
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)
    # print(creatures)

    while True:

        active_creature = random.choice(creatures)
        print('A {} from level {} has appeared from a dark and steamy forest.'.format(active_creature.name, active_creature.level))
        print()
        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')

        if cmd == 'a':
            hero.attack(active_creature)
        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('look around')
        else:
            print('OK, exiting game.')
            break

if __name__ == '__main__':
    main()