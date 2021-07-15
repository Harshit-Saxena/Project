import random

class Dice:
     def roll(self):   # Roll method created 
          first = random.randint(1,6)
          second = random.randint(1,6)
          print(f"The rolls were: ({first},{second})")

dice = Dice()
print(dice.roll())
print()
input("Press enter to exit !! ")