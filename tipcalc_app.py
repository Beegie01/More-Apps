from math import ceil

def calc_bill(bill, popl, sharing_formula):
    '''
    takes the bill amount, number of sharing parties
    and split by percentage share/sharing_formula (in decimal e.g 0.5 for 50%)
    '''

    perc = 0.18

    tip = bill*perc

    tot_bill = bill+tip

    each = ceil(tot_bill/popl)

    if sharing_formula != None:
        share_a = ceil(tot_bill*sharing_formula)

        share_b = ceil(tot_bill*(1 - sharing_formula))

    print(f"\n{perc*100}% tip: ${tip}\
    \nThis brings your otal to: ${tot_bill}\
    \nIf shared evenly:\
    \nEach pay: ${each}")
    if sharing_formula != None:
        print(f"\n\nUsing your given sharing formula:\
        \nOne person pays: ${share_a} ({sharing_formula*100}%)\
        \nThe other pays: ${share_b} ({100 - (sharing_formula*100)})%")

    perc = 0.20

    tip = bill*perc

    tot_bill = bill+tip

    each = ceil(tot_bill/popl)

    if sharing_formula != None:
        share_a = ceil(tot_bill*sharing_formula)

        share_b = ceil(tot_bill*(1 - sharing_formula))

    print(f"\n{perc*100}% tip: ${tip}\
    \nThis brings your otal to: ${tot_bill}\
    \nIf shared evenly:\
    \nEach pay: ${each}")
    if sharing_formula != None:
        print(f"\n\nUsing your given sharing formula:\
        \nOne person pays: ${share_a} ({sharing_formula*100}%)\
        \nThe other pays: ${share_b} ({100 - (sharing_formula*100)})%")

    perc = 0.25

    tip = bill*perc

    tot_bill = bill+tip

    each = ceil(tot_bill/popl)

    if sharing_formula != None:
        share_a = ceil(tot_bill*sharing_formula)

        share_b = ceil(tot_bill*(1 - sharing_formula))

    print(f"\n{perc*100}% tip: ${tip}\
    \nThis brings your otal to: ${tot_bill}\
    \nIf shared evenly:\
    \nEach pay: ${each}")
    if sharing_formula != None:
        print(f"\n\nUsing your given sharing formula:\
        \nOne person pays: ${share_a} ({sharing_formula*100}%)\
        \nThe other pays: ${share_b} ({100 - (sharing_formula*100)})%")
