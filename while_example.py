# you have 3 lives, i roll the dice, if i roll 6 you win, if not a 6 you lose a life

from random import randint

lives = 3

while lives > 0:
    roll = randint(1, 6)
    if roll == 6:
        print('You rolled a 6! You win!')
        break
    lives -= 1
    print(f'You rolled a {roll}, you lose a life')
    print(f'You have {lives} lives left')
else:
    print('You have no more lives, you lose!')
