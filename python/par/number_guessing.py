import random 

guess_the_number = random.randint(1,5)

while True:
 try:
    guess = int(input('Guess The Number Between 1 And 5 : '))

    if guess < guess_the_number:
        print('Too Low!')
    elif guess > guess_the_number:
        print('Too High!')
    else:
        print(' Wow You Guessed The Number. Congratulations!')
        break
 except ValueError:
    print('Enter a valid Number')


