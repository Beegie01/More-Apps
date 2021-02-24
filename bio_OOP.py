from datetime import datetime
import string

class Biography:

    def __init__(self):
        self.name = None
        self.dob = None
        self.addr = None
        self.goals = None

    def name_inp(self):
        prompt = "\nWhat is your name?\n>\t"

        while True:

            inp = input(prompt)

            if inp in string.punctuation:
                print("Error: Invalid Entry!")
                continue
            print("\n\nName Entered!")
            return inp.title()

    def dob_inp(self):
        print("\nWhat is your date of birth?")

        Yr = True
        prompt = "\nBirth Year\n>\t"
        while Yr:

            inp = input(prompt)

            try:
                yr = int(inp)

            except ValueError:
                print("Error: Invalid Entry!")
                continue

            if yr not in range(1920, 2021):
                print("Error: entry out of range!")
                continue
            print("Birth Year Entered!")
            Yr = False

        Mn = True
        prompt = "\nBirth Month\n>\t"
        while Mn:

            inp = input(prompt)

            try:
                mn = int(inp)

            except ValueError:
                print("Error: Invalid Entry!")
                continue

            if mn not in range(1, 13):
                print("Error: entry out of range!")
                continue
            print("Birth Month Entered!")
            Mn = False

        D = True
        prompt = "\nBirth Day\n>\t"
        while D:

            inp = input(prompt)

            try:
                day = int(inp)

            except ValueError:
                print("Error: Invalid Entry!")
                continue

            if day not in range(1, 32):
                print("Error: entry out of range!")
                continue
            print("Birth Day Entered!")
            D = False

        print("\n\nDate of Birth Entered!")
        return datetime.date(datetime(yr,mn,day))

    def addr_inp(self):

        prompt = "\nWhat is your address?\n>\t"

        while True:

            inp = input(prompt)

            if inp in string.punctuation:
                print("Error: Invalid Entry!")
                continue

            print("Address Entered!")
            return inp.title()

    def goal_inp(self):

        prompt = "\nWhat are your personal goals?\n>\t"

        while True:

            inp = input(prompt)

            if inp in string.punctuation:
                print("Error: Invalid Entry!")
                continue

            print("Goal Entered!")
            return inp.capitalize()

    def assign_bio(self):

        self.name = self.name_inp()

        self.dob = self.dob_inp()

        self.addr = self.addr_inp()

        self.goals = self.goal_inp()

    def view_bio(self):

        print(f"\n\n-\tName:\t{self.name}\
        \n-\tDate of Birth:\t{self.dob}\
        \n-\tAddress:\t{self.addr}\
        \n-\tPersonal Goals:\t{self.goals}")


    def ask_next(self):

        print("\n\nTo continue, enter 'y'\nTo stop, enter 'n'")
        prompt = '\nHave another?\n'
        acc_range = 'no yes'

        while True:
            inp = input(prompt)

            if inp.lower() not in acc_range:
                print("Error: Entry is invalid!")
                continue

            return inp.lower()
