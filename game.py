import random

import os

import dotenv

dotenv.load_dotenv()



player_name = os.getenv("player_name")
#print(player_name)

#more details on env variables in slack for 5/27 around 6:40 PM

#update the welcome to the game message so it's saying welcome player name
# remember player_name is a variable now

#wanna be cool? consider giving an option of doing single game or best out of three



print("Rock, Paper, Scissors, Shoot!") 

user_choice = input("Choose your weapon 'rock', 'paper', 'scissors':")

print("You chose: ", user_choice)


#Vvalidate the input such that only if it is one of the expected values
#...will we continue with the rest of the program
#...otherwise we'll stop the program before it tries to do anything else
#...and we'll ask the user to run the program again

#Consider adding some --------- to the code to space things out a bit nicer


if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("May the odds be ever in your favor")

else:
    print("OOPS, invalid input. Please try again.")
    exit()


valid_options=["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print("Robot Overlord Choice: ", computer_choice)

#Code suggestion of making user_choice==comp_choice attributed to Steven S.

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
    print("You win! Take that you filthy Robot!")
elif(user_choice == "scissors") and (computer_choice == "paper"):
    print("You win! Take that you filthy Robot!")
elif(user_choice == "rock") and (computer_choice == "scissors"):
    print("You win! Take that you filthy Robot!")

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")

