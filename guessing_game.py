import sys
sys.path.append('C:\\Users\\welcome\\Desktop\\MyFuncs')

from fave_app_funcs import *

from guessinggame_app import *

print("Welcome To the GUESSING GAME!!")

game = GuessingGame()

prompt = 'Please enter your name below\n>\t'
name = name_inp(prompt)

game.p1['name'] = name
START = True
while START:

    # collect names
    lim = (1,51)
    prompt = "\nPlease enter an integer below\nBetween 1-50\n>\t"
    game.p1['current_guess'] = num_inp(prompt, lim)

    # check for winner
    game.win_check()

    # score display
    game.scoreboard()

    ans = ask_next()

    if ans in 'yes':
        continue

    print("Thanks for playing!")
    GAME_ON = False
    START = False
