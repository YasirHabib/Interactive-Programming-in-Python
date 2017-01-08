# template for "Stopwatch: The Game"
import simplegui
# define global variables
t = 0
clicks = 0
correct_clicks = 0
boolean = True
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = "0"
    B = "0"
    C = "0"
    D = "0"
    if t < 10:
        D = str(t)
        return A+":"+B+C+"."+D
    elif t < 100: 
        C = str(t/10)
        D = str(t%10)
        return A+":"+B+C+"."+D   
    elif t < 600:
        B = str(t/100)
        R = t%100
        C = str(R/10)
        D = str(R%10)
        return A+":"+B+C+"."+D   
    else:
        A = str(t/600)
        R = t%600
        B = str(R/100)
        RR = R%100
        C = str(RR/10)
        D = str(R%10)
        return A+":"+B+C+"."+D
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global boolean
    boolean = True
    
def stop(): 
    global boolean
    if boolean == True:
        global correct_clicks
        global t
        if(t%10==0):
            correct_clicks = correct_clicks + 1
        global clicks
        clicks = clicks + 1
        timer.stop()
        boolean = False
    
def reset():
    timer.stop()
    global correct_clicks
    correct_clicks = 0
    global t 
    t = 0
    global clicks
    clicks = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t = t + 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), [100, 100], 30, "white")
    canvas.draw_text(str(correct_clicks)+"/"+str(clicks), [250, 20], 25, "green")

    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# create timer
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
