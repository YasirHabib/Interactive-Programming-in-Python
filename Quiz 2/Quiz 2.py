# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

number = 0
secret_number = 0
count = 7
# helper function to start and restart the game

def new_game():
    # initialize global variables used in your code here
    global count
    count = 7
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is", count
    print ""
    global secret_number   
    secret_number = random.randrange(0, 100)         
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global count
    count = 7
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is", count
    print ""
    global secret_number   
    secret_number = random.randrange(0, 100) 

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global count
    count = 10
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is", count
    print ""
    global secret_number   
    secret_number = random.randrange(0, 1000)  
    
    
def input_guess(guess):
    # main game logic goes here	
    global number
    global secret_number
    number = int(guess)
    # remove this when you add your code
    print "Guess was", number
    global count
    count = count - 1
    print "Number of remaining guesses is", count 
    if count == 0:
        if number == secret_number:
            print "Correct!"
            print ""
            new_game()
        else:
            print "You ran out of guesses. The number was", secret_number 
            print ""
            new_game()
    elif number < secret_number:
        print "Lower!"
        print ""
    elif number > secret_number:
        print "Higher!"
        print ""
    else:
        print "Correct!"
        print ""
        new_game()
   
# create frame
f = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
