import simplegui
import random, math

WIDTH=800
HEIGHT=600    

def draw(c):
    a=0
#    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
#    global lastWinner
       
            
    # draw ball
#    c.draw_circle(ball_pos, BALL_RADIUS, 1, "Orange", "Orange")
    
    
    # draw paddles
#    c.draw_line([HALF_PAD_WIDTH,paddle1_pos- HALF_PAD_HEIGHT], 
#                [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], 
#                PAD_WIDTH, "Orange")
    
    # draw scores
#    print_canvas_text(c, str(score1), 150, 120, 40, "Orange", "serif")
    
# Keydown handler.         
def keydown(key):
#    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
       cosa=0
        #        paddle2_vel = -3
#        tick_sound.play()
#    elif key == simplegui.KEY_MAP['down']:
#        paddle2_vel = 3
#        tick_sound.play()

# Keyup handler. 
def keyup(key):
    a=0
#    global paddle1_vel, paddle2_vel
#    if key == simplegui.KEY_MAP['up']:
#        paddle2_vel = 0
#    elif key == simplegui.KEY_MAP['down']:
#        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()


