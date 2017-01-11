import simplegui
import random

card_list = range(0, 8)
card_list1 = range(0, 8)
card_list2 = card_list + card_list1
random.shuffle(card_list2)

state = 0
counter = 0

exposed = [False, False, False, False, False, False, 
           False, False, False, False, False, False,
           False, False, False, False]

# helper function to initialize globals
def new_game():
    global counter
    global state
    global exposed
    for i in range(0, 16):              
        exposed[i] = False
    counter = 0
    state = 0
    label.set_text("Turns = " + str(counter))
    random.shuffle(card_list2)
    
# define event handlers
def mouseclick(pos):
    global X, Y, Z, exposed, state, first_card, second_card, counter 
    
    if state == 0:
        X = pos[0]
        X = X/50
        exposed[X] = True
        first_card = card_list2[X]
        state = 1
  
    elif state == 1:
        Y = pos[0]
        Y = Y/50
        exposed[Y] = True
        second_card = card_list2[Y]
        
        if (Y != X):
            state = 2
            counter = counter + 1
            label.set_text("Turns = " + str(counter))
             
    elif state == 2:
        Z = pos[0]
        Z = Z/50
        if ((Z != X) and (Z != Y)):             
        
            if first_card == second_card:
                exposed[X] = True
                exposed[Y] = True
            
            else:
                exposed[X] = False
                exposed[Y] = False
            
            exposed[Z] = True
            first_card = card_list2[Z]            
            X = Z
            state = 1
                           
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, card_list2
    card_pos = [0, 0]
    
    for i in range(0, 16):
        if exposed[i] == True:
            card = card_list2[i]																								
            canvas.draw_text(str(card), [card_pos[0] + 20, card_pos[1] + 70], 50, "White")
            card_pos[0] = card_pos[0] + 50
                   
        elif exposed[i] == False:
            canvas.draw_polygon([[card_pos[0], card_pos[1]], [card_pos[0] + 50, card_pos[1]], [card_pos[0] + 50, card_pos[1] + 100], [card_pos[0], card_pos[1] + 100]], 1, 'Yellow', 'Green')
            card_pos[0] = card_pos[0] + 50
     
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

frame.start()
