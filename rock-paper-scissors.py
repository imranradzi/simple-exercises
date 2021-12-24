import random

while True:
    choices = ['rock', 'paper', 'scissors']

    # gives values to each choice so we can compare them
    values = {'rock': 1, 'paper': 2, 'scissors': 3}

    # random choice for computer
    computer_choice = random.choice(choices)
    print(computer_choice)

    player_choice = input('rock, paper, or scissors?\n').lower()

    # stores player and computer choices
    pc_player_choice = {'player': player_choice, 'computer': computer_choice}

    # for when both choices are the same
    if values[pc_player_choice['player']] == values[pc_player_choice['computer']]:
        print('draw')
    # this is when player chooses rock, computer chooses scissors
    elif values[pc_player_choice['player']] - values[pc_player_choice['computer']] == -2:
        print('win')
    # and this is the reverse case
    elif values[pc_player_choice['player']] - values[pc_player_choice['computer']] == 2:
        print('lose')
    # the rest are the usual cases
    elif values[pc_player_choice['player']] > values[pc_player_choice['computer']]:
        print('win')
    else:
        print('lose')

    continue_or_not = input("continue? yes/no\n").lower()
    if continue_or_not != "yes":
        break
