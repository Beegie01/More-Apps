import string, random
class GuessingGame:

    def __init__(self):
        self.p1 = {'name': None, 'current_guess': None, 'games_won': 0, 'games_lost': 0, 'current_form': '', 'last_rounds_taken': 'Not win yet'}
        self.rounds_taken = 0
        self.round_num = 1


    def win_check(self):
        goal = random.randint(1,50)

        if goal != self.p1['current_guess']:
            print(f"\n\nOOPS!!\n{self.p1['name']}, {self.p1['current_guess']} WAS WRONG!\nYOU SHOULD HAVE GUESSED {goal}")
            self.round_num += 1
            self.rounds_taken += 1
            self.p1['games_lost'] += 1
            self.p1['current_form'] += 'L-'
        else:
            print(f"\n\nYAY!!\n{self.p1['name']}, {self.p1['current_guess']} WAS CORRECT\
            \nAFTER {self.rounds_taken} UNSUCCESSFUL ATTEMPTS")
            self.round_num += 1
            self.p1['games_won'] += 1
            self.p1['current_form'] += 'W-'
            self.p1['last_rounds_taken'] = self.rounds_taken
            self.rounds_taken = 0

    def scoreboard(self):

        print(f"\nGAME SCORE BOARD:\n\n\n{self.p1['name']}\n\tLAST GAME ROUND: {self.round_num-1}\
        \n\tROUNDS WON: {self.p1['games_won']}\
        \n\tPERFORMANCE: {self.p1['current_form'][:-1]}.")
