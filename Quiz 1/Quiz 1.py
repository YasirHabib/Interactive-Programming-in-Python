import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Error"


##########################################################
##########################################################
##########################################################

def number_to_name(name):
    if name == 0:
        return "rock"
    elif name == 1:
        return "Spock"
    elif name == 2:
        return "paper"
    elif name == 3:
        return "lizard"
    elif name == 4:
        return "scissors"
    else:
        print "Error"



##########################################################
##########################################################
##########################################################

def rpsls(player_choice): 
    
    print ""
    print "Player chooses", player_choice 
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice 

    if (comp_number - player_number) % 5 == 1:
        print "Computer wins!"
        
    elif (comp_number - player_number) % 5 == 2:
        print "Computer wins!"  
        
    if (comp_number - player_number) % 5 == 3:
        print "Player wins!"
        
    if (comp_number - player_number) % 5 == 4:
        print "Player wins!"
    
    elif (comp_number - player_number) % 5 == 0:
        print "Player and computer tie!"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


