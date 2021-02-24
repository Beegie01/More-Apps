import sys
sys.path.append('C:\\Users\\welcome\\Desktop\\MyFuncs')

from mylist_funcs import counter_od

def word_inp():

    prompt = "\nWhat's on your mind today?\
    \n>\t"
    while True:
        inp = input(prompt)

        if not(inp.isprintable()):
            print(f"\nInvalid entry!")
            continue

        return inp.capitalize()

def split(text, sep):

    if sep not in text:
        print()
        return f"'{sep}' not found in text"

    coordinates = []
    word_list = []

    # capturing the indices of each whitespaces in the text
    for ind in range(len(text)):
        if text[ind] in sep:
            coordinates.append(ind)

    # in case there is no whitespace at end of text
    if coordinates[-1] != len(text):
        coordinates.append(len(text))

    # to map out each words according to list of coordinates/coordinates
    for num, ind in enumerate(coordinates):
        if num == 0:
            word_list.append(text[:coordinates[num]])
            continue
        word_list.append(text[(coordinates[(num-1)]+1) : coordinates[num]])

    return word_list

def word_out():
    ans = word_inp()

    ans_list = split(ans, ' ')

    result = counter_od(ans_list)
    print(f"\n\nYou just told what was on your mind in {len(ans_list)} words")
    print(f"The frequency of each word are:\n{result}")


def ask_next():
    print("\n\nTo continue, enter 'y'\nTo stop, enter 'n'")
    prompt = '\nHave another?\n'
    acc_range = 'no yes'
    while True:
        inp = input(prompt)

        if inp.lower() not in acc_range:
            print("Error: Entry is invalid!")
            continue

        return inp.lower()
