from bio_OOP import Biography

while True:
    print("Welcome!!")

    bio = Biography()

    bio.assign_bio()

    bio.view_bio()

    ans = bio.ask_next()

    if ans in 'yes':
        continue

    break
