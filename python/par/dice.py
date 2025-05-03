import random

while True:
         choice = input('Roll The Dice (y/n): ').lower()
         if choice == 'y':
            roll = random.randint(1,6)
            rol2 = random.randint(1,6)
            print(f'({roll},{rol2})')
         elif choice == 'n':
           print("Thnak You For Playing With Us.")
           break
         else:
           print("Enter Velid Choice.") 
           