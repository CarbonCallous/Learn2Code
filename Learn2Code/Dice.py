import random # import random

#define main and pass roll and sides
def main (roll, sides):
    print("You have rolled a ",sides," sided die, and it landed on ",roll,"!") #print results and call the function to repeat game
    again()

def again():#function to repeat
    playAgain = input("Would you like to roll again? y or n? ")#ask if user wants to repeat
    if (playAgain == "y"):#if yes, call game from start
        sidesDice()
    elif (playAgain == "n"):#if no, end game
        print("Have a nice day!")
    else: #if out of bounds, recalls current function
        print("Try again: ")
        again()


def diceRoll (sides):#actual roll based on user input of sides
    roll = random.randint(1,sides); #uses random up to user input to select a number as roll
    main(roll,sides) #calls main function

def sidesDice(): #function that starts game
    sides = input("How many sides should the die be? (1-20)"); #ask user for input
    sides = int(sides); #convert from string to integer
    diceRoll(sides) #call next function and pass variable


sidesDice() #calls first function