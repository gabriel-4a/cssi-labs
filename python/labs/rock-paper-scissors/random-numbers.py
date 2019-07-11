import random

print("Welcome to Gabriel's random playground")

die1 = random.randint(1,6)
die2 = random.randint(1,6)

sum = die1 + die2

if die1 == die2:
    print("You got DOUBLES!!!!")
    print("This is your sum:  %s " % (sum))
    print("Roll again")

else:
    print("you get to move %s steps" % (sum))
    print("Next players turn!!")
