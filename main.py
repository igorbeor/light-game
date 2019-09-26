from time import sleep
from random import choice
from character import Character


def main():
    computer = Character('Computer')
    user = Character(input('Type name of your character: '))

    # randomly selects a sequence of moves
    turn = choice(['user', 'computer'])

    # the game ends when one of the characters runs out of health points
    while user.health_point > 0 and computer.health_point > 0:
        if turn == 'user':
            turn = 'computer'
            move = input('Enter choice: ')
            if move == '1':
                damage = user.deal_medium_damage_range(computer)
                print('You inflicted {} damage to the enemy.'.format(damage))
            elif move == '2':
                damage = user.deal_high_damage_range(computer)
                print('You inflicted {} damage to the enemy.'.format(damage))
            elif move == '3':
                heal = user.heal_yourself()
                print('You have restored your character {} health points.'
                    .format(heal))
            else:
                print('Enter a valid selection')
                turn = 'user'
        else:
            turn = 'user'
            list_of_moves = ['1', '2', '3']
            
            # if the enemy’s health points fall below 35, then the computer
            # increases the chance to restore health points 
            if computer.health_point <= 35:
                list_of_moves = ['1', '2', '3', '3', '3']
            move = choice(list_of_moves)
            if move == '1':
                damage = computer.deal_medium_damage_range(user)
                print('The enemy has dealt you {} damage.'.format(damage))
            if move == '2':
                damage = computer.deal_high_damage_range(user)
                print('The enemy has dealt you {} damage.'.format(damage))
            if move == '3':
                heal = computer.heal_yourself()
                print('The enemy has restored his character {} health points.'
                    .format(heal))
        print('{}: {}HP\nComputer: {}HP\n'.format(user.name, user.health_point, computer.health_point))
        sleep(2.0)

    if user.health_point > computer.health_point:
        print('YOU WIN!')
    else:
        print('YOU LOSE :(')

if __name__ == "__main__":
    main()
