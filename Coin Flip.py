import random
#importing random

#defining as a module so it can loop
def main(): 
    flip = 0;
    #ask user if they want to flip
    userInput = input("Flip a coin, heads or tails? Y for yes: N for no: ");
    #check user input for continuing to run
    if (userInput == "y"):
        flip = random.randint(0,100); #set the random integer and check if it should be heads or tails
        if (flip <= 51):
            print ("The coin landed on heads!");
            main() # calls the module again to repeat
        elif (flip > 51):
            print ("The coin landed on tails!");
            main()
    elif (userInput == "n"): #exit message
        print("Have a great day! \nExiting now");
    else: 
        print("I did not recognize your input")
        main()
        

    
#initial call
main()