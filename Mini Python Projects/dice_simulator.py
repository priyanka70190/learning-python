import random

class Dice:
    def __init__(self,no_of_dice):
        self.no_of_dice = no_of_dice

    def roll(self):
       if self.no_of_dice == 1:
           die=random.randint(1,6)
           print("value on die1:",die)
       else:
           die1=random.randint(1,6)
           die2=random.randint(1,6)
           #print("value on die1:",die1)
           #print("value on die2:",die2)
           print("you rolled ",die1,"and ",die2)

print("How many Dice do you want to roll?(1 or 2):")
no_of_dice = int(input())
dice=Dice(no_of_dice)

while(True):
    print("Dice Simulator ready!press 'Enter' to roll dice or press 'end,done,quit,escape,close'")
    choice=input().strip()
    if choice == 'end'or choice == 'done'or choice == 'quit' or choice == 'escape'or choice == 'close':
        print("Thanks for playing,Good Bye!")
        break
    elif choice == "":
        print("user pressed enter")
        dice.roll()


