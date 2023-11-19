import random

def instructions():
    print('\nWelcome to Rock, Paper, Scissors!\nThe game is simple\nYou are going to play rock, paper, scissors against the computer\nJust input what you want to play and soon enough you will know if you won\nGood Luck!')

def game():
    choice =  input('\nEnter rock paper or scissors: \n')
    pc_play = random.randint(0,2)

    if pc_play == 0:
        pc_play = 'rock'
    elif pc_play == 1:
        pc_play = 'paper'
    else:
        pc_play = 'scissors'

    if pc_play == choice:
        print('Game Over! You ended in a tie')
    elif pc_play == 'rock' and choice == 'paper':
        print(f'You win! {choice} wins against {pc_play}!')
    elif pc_play == 'rock' and choice == 'scissors':
        print(f'Game Over! {pc_play} wins against {choice}!')
    elif pc_play == 'paper' and choice == 'scissors':
        print(f'You win! {choice} wins against {pc_play}!')
    elif pc_play == 'paper' and choice == 'rock':
        print(f'Game Over! {pc_play} wins against {choice}!')
    elif pc_play == 'scissors' and choice == 'rock':
        print(f'You win! {choice} wins against {pc_play}!')
    elif pc_play == 'scissors' and choice == 'paper':
        print(f'Game Over! {pc_play} wins against {choice}!')

instructions()
game()