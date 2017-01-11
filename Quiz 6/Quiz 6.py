# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
msg = ""
msg1 = ""
score = 0
player_h = []
dealer_h = []
deck = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.card = []

    def __str__(self):
        ans = ""
        for i in range(len(self.card)):
            ans += str(self.card[i])
            ans = ans + " "
        return ans
        
    def add_card(self, card):
        self.card.append(card)

    def get_value(self):
        value = 0
        Flag = False
        
        for i in self.card:            
            value += VALUES[i.get_rank()]
            if i.get_rank() == 'A':
                Flag = True
        
        if Flag == False:
            return value
        
        else:
            if value + 10 > 21:
                return value
            
            else:
                return value + 10
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in self.card:
            x = self.card.index(i)
            self.card[x].draw(canvas, [ pos[0] + x * 100, pos[1]])
         
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        
        for i in SUITS:
            for j in RANKS:
                test = Card(i , j)
                self.deck.append(test)
                                 
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(len(self.deck)-1)
        
    def __str__(self):
        Z = []
        for test  in self.deck:
            Z.append(str(test))
        return str(Z)

#define event handlers for buttons
def deal():
    global outcome, in_play, player_h, dealer_h, deck, msg, msg1, score
    
    if in_play == True:
        score -= 1
        
    in_play = True
    outcome = ""
    
    deck = Deck()
    deck.shuffle()
    
    player_h = Hand()
    dealer_h = Hand()
    
    for i in range(2):
        c1 = deck.deal_card()
        player_h.add_card(c1)
    
        c2 = deck.deal_card()
        dealer_h.add_card(c2)    
    
    msg = "Hit or stand?"
    msg1 = ""
    
def hit():
    global in_play, score, msg, msg1
    
    if player_h.get_value() <= 21:
        c1 = deck.deal_card()
        player_h.add_card(c1)
        
        if player_h.get_value() > 21:
            msg = "You busted."
            msg1 = "New Deal?"
            in_play = False
            score -= 1
       
def stand():
    # replace with your code below
    global in_play, score, msg, msg1
    in_play = False
    if player_h.get_value() > 21:
        msg = "You busted"
        msg1 = "New Deal?"
    else:
         while dealer_h.get_value() < 17:
            c1 = deck.deal_card()
            dealer_h.add_card(c1)
        
         if dealer_h.get_value() > 21:
            msg = "Dealer busts. You win."
            msg1 = "New Deal?"
            score += 1
         else:
            if player_h.get_value() <= dealer_h.get_value():
                msg = "Dealer wins."
                msg1 = "New Deal?"
                score -= 1
            else:
                msg = "You win."
                msg1 = "New Deal?"
                score += 1

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    dealer_h.draw(canvas, [100, 200])
    player_h.draw(canvas, [100, 400])
    canvas.draw_text(str(msg), (225, 375), 30, "Red")
    canvas.draw_text(str(msg1), (100, 550), 30, "Red")
    canvas.draw_text("Blackjack", (250, 50), 30, "Red")
    canvas.draw_text("Dealer", (100, 175), 30, "Red")
    canvas.draw_text("Player", (100, 375), 30, "Red")
    canvas.draw_text("Score: "+str(score), (260, 100), 30, "Red")
    
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (100 + CARD_CENTER[0], 200 + CARD_CENTER[1]), CARD_BACK_SIZE) 

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling

frame.start()
deal()

# remember to review the gradic rubric
