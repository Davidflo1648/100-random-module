import random

def game():
    choice = input('\nChoose Heads or Tails: ')

    coin = random.randint(0,1)

    if coin == 0:
        result = 'heads'
    elif coin == 1:
        result = 'tails'

    if result == choice:
        print(f'You won! The coin landed on {result}.')
    else:
        print(f'Game Over! The coin landed on {result} and you guessed {choice}')
