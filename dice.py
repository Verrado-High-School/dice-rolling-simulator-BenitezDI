# Name: Dayanara 
# Period 6 
# Dice Rolling Simulator

import random 

side1 = 0 
side2 = 0
side3 = 0
sied4 = 0 
side5 = 0 
side6 = 0
rolls = random.randint(1,6)

print("Hello human being of this earth. Welcome tooooooo Dice Rolling Simulator!")
roll = int(input (" How many time would like to roll the dice?: "))
x = 1
while x<= roll:
  if rolls == 1:
    side1 += 1
  elif roll == 2:
    side2 += 1
  elif roll == 3:
    side3 += 1
  elif roll == 4:
    side4 += 1
  elif roll == 5:
    side5 += 1
  else:
    side6 += 1

  x = x+1
