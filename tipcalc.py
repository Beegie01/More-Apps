# importing path from the sys module
from sys import path    # path is a built-in mutable sequence

# adding 'MyFuncs' package to the list of searchable paths for Python
path.append('C:\\Users\\welcome\\Desktop\\MyFuncs')

from fave_app_funcs import float_inp, num_inp, ask_next

from tipcalc_app import *

print("Welcome!!!\n\nTipCalc\n")

while True:
    prompt = "\nWhat's the total bill for today, please?\n>\t"
    bill = float_inp(prompt)

    prompt = "\nHow many parties shall be sharing this bill?\n>\t"
    pple = num_inp(prompt)

    share = None

    if pple == 2:
        prompt = "\nBy what percentage do you want your bill to be split?\n>\t"
        share = float_inp(prompt, (0.0,1.01), 0.1)

    calc_bill(bill, pple, share)

    ans = ask_next()

    if ans in 'yes':
        continue

    print("\n\nThank you for using this app!\n\nExiting app")
    break
