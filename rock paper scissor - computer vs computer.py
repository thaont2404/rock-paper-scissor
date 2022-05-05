# ROCK-PAPER-SCISSOR CO vs CO
from random import choice

# input name of 2 computers
computer1_name = input('Your first gladiator: ').title()
computer2_name = input('Your second gladiator: ').title()

# begin point
computer2_score = 0
computer1_score = 0
# computer2 game -> input
game_active = True
while game_active:
    # computer1 game -> random choice
    print('──────────────────────────')
    computer1_choose = ['rock', 'paper', 'scissor']
    computer1 = choice(computer1_choose)
    print(f'{computer1_name} choose: {computer1.upper()}')

    # computer2 game -> random choice
    computer2_choose = ['rock', 'paper', 'scissor']
    computer2 = choice(computer1_choose)
    print(f'{computer2_name} choose: {computer1.upper()}')
    print('──────────────────────────')
    
    # # who wins? --> using if, elif, else to determine the winner by using the basic rules of rock-paper-scissor
    if computer1 == 'scissor':
        if computer2 == 'paper':
            print(f'{computer2_name} loss ಥ_ಥ')
            computer1_score += 1
        elif computer2 == 'rock':
            print(f'{computer2_name} win (((o(*ﾟ▽ﾟ*)o)))')
            computer2_score += 1
        else:
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
    elif computer1 == 'rock':
        if computer2 == 'paper':
            print(f'{computer2_name} win (((o(*ﾟ▽ﾟ*)o)))')
            computer2_score += 1
        elif computer2 == 'rock':
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
        else:
            print(f'{computer2_name} loss ಥ_ಥ')
            computer1_score += 1
    elif computer1 == 'paper':
        if computer2 == 'paper':
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
        elif computer2 == 'rock':
            print(f'{computer2_name} loss ಥ_ಥ')
            computer1_score += 1
        else:
            print(f'{computer2_name} win (((o(*ﾟ▽ﾟ*)o)))')
            computer2_score += 1
    
    # score broad -> print computer2 score and computer1 score after each round
    print(f'{computer1_name.upper()} SCORE: {computer1_score}\n{computer2_name.upper()} SCORE: {computer2_score}\n──────────────────────────')

    # user input N/NO to quit the game --> after user quit, print 'GAME OVER'
    continue_play = input('Watch them fight to death? Y (YES) /N (NO): ')
    if continue_play.upper() == 'N' or continue_play.upper() == 'NO':
        print(f'───────────────\nFINAL SCORE: {computer2_score} - {computer1_score}')
        if computer2_score > computer1_score:
            print(f'The win belongs to: {computer2_name} (((o(*ﾟ▽ﾟ*)o)))')
        elif computer1_score < computer2_score:
            print(f'The win belongs to: {computer1_name} (((o(*ﾟ▽ﾟ*)o)))')
        elif computer1_score == computer2_score:
            print('It\'s a tie ( ͡° ͜ʖ ͡°)')
        print('───────────────')
        game_active = False
        print('GAME OVER')
