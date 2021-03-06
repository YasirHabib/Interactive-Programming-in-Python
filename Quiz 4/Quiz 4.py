# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

score1 = 0
score2 = 0

paddle1_pos = (HEIGHT / 2) - HALF_PAD_HEIGHT
paddle2_pos = (HEIGHT / 2) - HALF_PAD_HEIGHT

paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    
    x = random.randrange(2, 4)
    y = random.randrange(2, 4)
    
    if direction == RIGHT:
        ball_vel = [x, -y]
    
    elif direction == LEFT:
        ball_vel = [-x, -y]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = (HEIGHT / 2) - HALF_PAD_HEIGHT
    paddle2_pos = (HEIGHT / 2) - HALF_PAD_HEIGHT
    
    paddle1_vel = 0
    paddle2_vel = 0
    
    score1 = 0
    score2 = 0
    
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    
          
     
    
    if (ball_pos[0] - PAD_WIDTH) < BALL_RADIUS:
        
        if ((ball_pos[1] + BALL_RADIUS) < paddle1_pos):
            score2 = score2 + 1
            spawn_ball(RIGHT)
    
        elif ((ball_pos[1] - BALL_RADIUS) < (paddle1_pos + PAD_HEIGHT)):
            ball_vel[0] = -1.2*ball_vel[0]
            
    
        else:
            score2 = score2 + 1
            spawn_ball(RIGHT)
    
    elif ((WIDTH - PAD_WIDTH) - ball_pos[0]) < BALL_RADIUS:
        
        if ((ball_pos[1] + BALL_RADIUS) < paddle2_pos):
            score1 = score1 + 1
            spawn_ball(LEFT)
    
        elif ((ball_pos[1] - BALL_RADIUS) < (paddle2_pos + PAD_HEIGHT)):
            ball_vel[0] = -1.2*ball_vel[0]
    
        else:
            score1 = score1 + 1
            spawn_ball(LEFT)
        
        
    elif (HEIGHT - ball_pos[1]) < BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    elif ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = paddle1_pos + paddle1_vel
    paddle2_pos = paddle2_pos + paddle2_vel 
    
    if paddle1_pos == 0:
        paddle1_vel = 0
    
    elif paddle1_pos == HEIGHT - PAD_HEIGHT:
        paddle1_vel = 0
        
    if paddle2_pos == 0:
        paddle2_vel = 0
        
    elif paddle2_pos == HEIGHT - PAD_HEIGHT:
        paddle2_vel = 0    
    
    
    # draw paddles
    canvas.draw_line([0, paddle1_pos], [0, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH, paddle2_pos], [WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "White")

    # draw scores
    canvas.draw_text(str(score1), [200, HEIGHT / 4], 30, "White")
    canvas.draw_text(str(score2), [400, HEIGHT / 4], 30, "White")

        
def keydown(key):
    global paddle1_vel, paddle2_vel
    v = 4
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = paddle1_vel - v
        
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle1_vel + v
        
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = paddle2_vel - v
        
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle2_vel + v    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button("Restart", new_game, 100)

# start frame
new_game()
frame.start()
