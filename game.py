import random

import os

import dotenv

dotenv.load_dotenv()



player_name = os.getenv("player_name")

print("------------------------")
print("Welcome",player_name,"to my Rock-Paper-Scissors game!") 
print("------------------------")

user_choice = input("Choose your weapon 'rock', 'paper', or 'scissors':")

print("You chose: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("May the odds be ever in your favor")

else:
    print("OOPS, invalid input. Please try again.")
    exit()


valid_options=["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print("Robot Overlord Chose: ", computer_choice)
print("------------------------")

# Draw
# Code suggestion of making user_choice==comp_choice attributed to Steven S.

if (computer_choice==user_choice):
    print("It's a draw!")

#Computer Wins

elif(user_choice == "scissors") and (computer_choice == "rock"):
    print("Robot Overlord wins! Better luck next time.")
elif(user_choice == "paper") and (computer_choice == "scissors"):
    print("Robot Overlord wins! Better luck next time.")
elif(user_choice == "rock") and (computer_choice == "paper"):
    print("Robot Overlord wins! Better luck next time.")

#Player Wins

elif(user_choice == "paper") and (computer_choice == "rock"):
    print("You win! Take that filthy Robot!")
elif(user_choice == "scissors") and (computer_choice == "paper"):
    print("You win! Take that filthy Robot!")
elif(user_choice == "rock") and (computer_choice == "scissors"):
    print("You win! Take that filthy Robot!")

print("------------------------")

print("Thanks for playing. Please play again!")

