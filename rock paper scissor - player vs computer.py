# ROCK-PAPER-SCISSOR CO vs USER
from random import choice

# player game -> input
game_active = True
while game_active:
    player = input('Choose: \n\tR - Rock\n\tP - Paper\n\tS - Scissor\n\t... ')

    # return player choice
    if player.lower() == 'r' or player.lower() == 'rock':
        player = "rock"
    elif player.lower() == 'p' or player.lower() == 'paper':
        player = "paper"
    else:
        player = "scissor"
    print(f'You choose: {player.upper()}')

    # computer game -> random choice
    computer_choose = ['rock', 'paper', 'scissor']
    computer = choice(computer_choose)
    print(f'The computer choose: {computer.upper()}')
    print('---------------------------')

    # who wins?
    if computer == 'scissor':
        if player == 'paper':
            print('You loss ಥ_ಥ')
        elif player == 'rock':
            print('You win (((o(*ﾟ▽ﾟ*)o)))')
        else:
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
    elif computer == 'rock':
        if player == 'paper':
            print('You win (((o(*ﾟ▽ﾟ*)o)))')
        elif player == 'rock':
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
        else:
            print('You loss ಥ_ಥ')
    elif computer == 'paper':
        if player == 'paper':
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
        elif player == 'rock':
            print('You loss ಥ_ಥ')
        else:
            print('You win (((o(*ﾟ▽ﾟ*)o)))')

    continue_play = input('Continue playing? Y (YES) /N (NO): ')
    if continue_play.upper() == 'N' or continue_play.upper() == 'NO':
        game_active = False
        print('GAME OVER')
