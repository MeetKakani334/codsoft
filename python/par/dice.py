import random

choice = input('Roll The Dice (y/n): ').lower()
if choice == "y":
   roll = random.randint(1,6)
   rol2 = random.randint(1,6)
   print(f'({roll},{rol2})')
