print("Rock, Paper, Scissors, Shoot!") 

user_choice = input("Choose your weapon 'rock', 'paper', 'scissors':")

print("You chose: ", user_choice)
print("May the odds be ever in your favor")


#Vvalidate the input such that only if it is one of the expected values
#...will we continue with the rest of the program
#...otherwise we'll stop the program before it tries to do anything else
#...and we'll ask the user to run the program again



if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()
print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")