# import random

# def rps():
#  return random.choice(["rock,peper,secissor"])


# def work(user ,computer):
#     user = str(input("enter rock,peper,secissor"))
#     if user == computer:
#        print("tie")
#     elif user == "rock" and computer == "secissor":
#        print("you won")
#     elif user == "secissor" and computer == "peper":
#        print("you won")
#     elif user == "peper" and computer == "rock":
#        print("you won")
#     else:
#        print("you lose")

# def game():
   
      
      
    
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()
        if player_choice == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)

# Start the game
play_game()

