import random

def guess(x):
    r1 = random.randint(1,9)
    guess = 0
    while guess != r1:
        guess = int(input('guess a number between 1 and 9'))
        if guess < r1:
            print('sorry, wrong number guess again too low.')
        elif guess > r1:
            print('sorry wrong number guess again too high.')

    print('Yay, nice. You have guessed the number correctly')


guess(10) 


