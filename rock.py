
#R-for rock
#P- for paper
#S- for scissor

import random

while True:

    user_input=input("Enter R for Rock ,P for Paper,S for Scissor:").upper()
    option=['R','P','S']
    computer=random.choice(option)

    if  user_input.upper() not in option:
        print("Wrong Input! Plz Try Again")

    else:
        if user_input==computer:
            print("It is a Tie")
    
        elif user_input=="R":
            if computer=="S":
                print("Rock Smashed Sissors , You Win")
            else:
                print("Paper Covers Rock , You Lose")

        elif user_input=="P":
            if computer=="R":
                print("Paper Covers Rock , You Win")

            else:
                print("Scissors Cuts Paper , You Lose")
    
        elif user_input=="S":
            if computer=="P":
                print("Scissors Cuts Paper ,You Win")
        
            else:
                print("Rock Smashed Scissors, You Lose")
    
    
    
        