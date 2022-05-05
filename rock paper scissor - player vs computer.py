# ROCK-PAPER-SCISSOR CO vs USER
from random import choice
player_name = input('Welcome player ᕙ(⍢)ᕗ\nEnter your name: ')
print(f'CHALLENGER {player_name.upper()}, LET\'S THE GAME BEGIN!')
player_score = 0
computer_score = 0
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
    print('──────────────────────────')

    # # who wins? --> using if, elif, else to determine the winner by using the basic rules of rock-paper-scissor
    if computer == 'scissor':
        if player == 'paper':
            print('You loss ಥ_ಥ')
            computer_score += 1
        elif player == 'rock':
            print('You win (((o(*ﾟ▽ﾟ*)o)))')
            player_score += 1
        else:
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
    elif computer == 'rock':
        if player == 'paper':
            print('You win (((o(*ﾟ▽ﾟ*)o)))')
            player_score += 1
        elif player == 'rock':
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
        else:
            print('You loss ಥ_ಥ')
            computer_score += 1
    elif computer == 'paper':
        if player == 'paper':
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
        elif player == 'rock':
            print('You loss ಥ_ಥ')
            computer_score += 1
        else:
            print('You win (((o(*ﾟ▽ﾟ*)o)))')
            player_score += 1

    # score broad -> print player score and computer score after each round
    print(f'{player_name.upper()} SCORE: {player_score}\nENEMY SCORE: {computer_score}\n──────────────────────────')
    # user input N/NO to quit the game --> after user quit, print 'GAME OVER'
    continue_play = input('Continue playing? Y (YES) /N (NO): ')
    if continue_play.upper() == 'N' or continue_play.upper() == 'NO':
        print(f'───────────────\nFINAL SCORE: {player_score} - {computer_score}')
        if player_score > computer_score:
            print('You loss ಥ_ಥ')
        elif computer_score < player_score:
            print('You win (((o(*ﾟ▽ﾟ*)o)))')
        elif computer_score == player_score:
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
        print('───────────────')
        game_active = False
        print('GAME OVER')
    