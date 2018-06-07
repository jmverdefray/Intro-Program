### Mini-project #4 - "Pong" #######################
### Nitin Kumar Jain ###############################

#### Assumptions ###################################
# 1. We only need to increase horizontal speed #####
# and not the vertical speed #######################
# 2. The ball spawns moving towards the player #####
# that won the last point. #########################
####################################################

# Implementation of classic arcade game Pong
import simplegui
import random, math

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
BALL_LEFT_LIMIT = BALL_RADIUS + PAD_WIDTH
BALL_RIGHT_LIMIT = WIDTH - BALL_RADIUS - PAD_WIDTH
BALL_TOP_LIMIT = BALL_RADIUS
BALL_BOTTOM_LIMIT = HEIGHT - BALL_RADIUS
#ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [2, 1] #Random value will be chosen in spawn_ball()
isGamePaused = False
flashcount = 0
leftSideColorFlash = "Black"
rightSideColorFlash = "Black"
lastWinner = "None"
flashAltColor = "Red"
tick_sound_url='http://themushroomkingdom.net/sounds/wav/smw/smw_kick.wav'
ball_missed_sound_url='http://themushroomkingdom.net/sounds/wav/nsmb_boo.wav'
pad_hit_url='http://themushroomkingdom.net/sounds/wav/m&lss_jump.wav'


def handle_flashtimer():
    # This function will have a red flash on loser side. 
    global flashcount, leftSideColorFlash, rightSideColorFlash, lastWinner

    if flashtimer.is_running():
        
        if flashcount >= 6:
            flashtimer.stop()
            flashcount = 0
            leftSideColorFlash = "Black"
            rightSideColorFlash = "Black"
            lastWinner = "None"
        else:
            if (flashcount % 2) == 0:
                if lastWinner == "Player1":
                    leftSideColorFlash = flashAltColor
                elif lastWinner == "Player2":
                    rightSideColorFlash = flashAltColor
            else:
                leftSideColorFlash = "Black"
                rightSideColorFlash = "Black"
            flashcount += 1

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    #Randomly generating horizontal velocity
    ball_vel[0] = float (random.randrange(120, 240)) / 60 
    if direction == LEFT:
        ball_vel[0] = - ball_vel[0]
    
    #Randomly generating vertical velocity
    ball_vel[1] =   float(- random.randrange (60, 180)) / 60
  

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global isGamePaused
    
    #Initializing all variables and spawn ball
    # Reseting game to not paused mode
    isGamePaused = False
    pause_button.set_text("Pause (p)")
    # Reseting scores at starte of game
    score1, score2 = 0, 0
    # Reseting paddle position and velocity at start of game
    paddle1_pos, paddle2_pos = HEIGHT / 2, HEIGHT / 2
    paddle1_vel, paddle2_vel = 0, 0
    # Randomly choosing direction of ball
    spawn_ball(random.choice([LEFT, RIGHT]))
    
def pause_game():
    # This function pauses game in case you want to take a coffee break. :)
    global isGamePaused
    isGamePaused = not isGamePaused
    if isGamePaused:
        pause_button.set_text("Resume (p)")
    else: 
        pause_button.set_text("Pause (p)")
        
def print_canvas_text(canvas, text, center_x, y, fontsize, fontcolor, fontface):
    # This utility prints on canvas by taking midpoint in x co-ordinate.
    # It is wrapper on existing draw_text. 
    len_text = frame.get_canvas_textwidth(text, fontsize, fontface)
    start_x = math.ceil(center_x - 0.5*len_text)
    canvas.draw_text(text, [start_x, y], fontsize, fontcolor, fontface)

        
    

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global lastWinner
    
    # Painting either side of board differently with flash
    c.draw_polygon([[0, 0], [WIDTH/2, 0], [WIDTH/2, HEIGHT], [0, HEIGHT]], 1, 
                   leftSideColorFlash, leftSideColorFlash)
    c.draw_polygon([[WIDTH/2, 0], [WIDTH, 0], [WIDTH, HEIGHT], [WIDTH/2, HEIGHT]], 1, 
                   rightSideColorFlash, rightSideColorFlash)
    
    print_canvas_text(c, "P O N G", 300, 300, 120, "Gray", "monospace")
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    # updating ball and pads only when game is not paused
    if not isGamePaused:
        
        # Calculating new position of ball
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
        
        #Determing when Ball hits Left gutter/pad
        if (ball_pos[0] < BALL_LEFT_LIMIT):
            # Determing if ball didn't hit the pad
            if ball_pos[1] < (paddle1_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle1_pos + HALF_PAD_HEIGHT):
                spawn_ball(RIGHT)
                score2 += 1
                lastWinner = "Player1"
                flashtimer.start()
                ball_missed_sound.play()    
                
             # Else it hit pad
            else:
                # Intentionally only increasing horizontal velocity
                ball_vel[0] = - 1.1 * ball_vel[0]
                pad_hit_sound.play()
    #            ball_vel[1] = 1.1 * ball_vel[1]
    
        #Determing when Ball hits right gutter/pad
        if (ball_pos [0] > BALL_RIGHT_LIMIT):
            
            # Determing if ball didn't hit the pad
            if ball_pos[1] < (paddle2_pos - HALF_PAD_HEIGHT) or ball_pos[1] > (paddle2_pos + HALF_PAD_HEIGHT):
                spawn_ball(LEFT)
                score1 += 1
                lastWinner = "Player2"
                flashtimer.start()
                ball_missed_sound.play()    
            # Else it hit pad
            else: 
                # Intentionally only increasing horizontal velocity
                ball_vel[0] = - 1.1 * ball_vel[0]
                pad_hit_sound.play()
    #            ball_vel[1] = 1.1 * ball_vel[1]
        
        if (ball_pos[1] < BALL_TOP_LIMIT) or (ball_pos[1] > BALL_BOTTOM_LIMIT):
            ball_vel[1] = - ball_vel[1]
            pad_hit_sound.play()
        
            
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "Orange", "Orange")
    
    # update paddle's vertical position, keep paddle on the screen
    if not isGamePaused:
        if paddle1_pos + paddle1_vel > HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel < HEIGHT - HALF_PAD_HEIGHT:
            paddle1_pos = paddle1_pos + paddle1_vel
            
        if paddle2_pos + paddle2_vel > HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel < HEIGHT - HALF_PAD_HEIGHT:
            paddle2_pos = paddle2_pos + paddle2_vel
    
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH,paddle1_pos- HALF_PAD_HEIGHT], 
                [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], 
                PAD_WIDTH, "Orange")

    c.draw_line([WIDTH - HALF_PAD_WIDTH,paddle2_pos- HALF_PAD_HEIGHT], 
                [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 
                PAD_WIDTH, "Orange")
    
    # draw scores
    print_canvas_text(c, str(score1), 150, 120, 40, "Orange", "serif")
    print_canvas_text(c, "Player 1", 150, 80, 24, "Orange", "serif")
    print_canvas_text(c, str(score2), 450, 120, 40, "Orange", "serif")
    print_canvas_text(c, "Player 2", 450, 80, 24, "Orange", "serif")
    
# Keydown handler.         
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -3
        tick_sound.play()
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 3
        tick_sound.play()
    elif key == simplegui.KEY_MAP['w']: 
        paddle1_vel = -3
        tick_sound.play()
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 3
        tick_sound.play()
    elif key == simplegui.KEY_MAP['p'] or key == simplegui.KEY_MAP['space']:
        # Using space or p for pause. But only marking p on screen
        # for pause. space pause is hidden feature.
        pause_game()
    elif key == simplegui.KEY_MAP['r']:
        new_game()

# Keyup handler. 
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
        
    elif key == simplegui.KEY_MAP['w']: 
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart (r)", new_game, 100) 
frame.add_label(" ")
pause_button = frame.add_button("Pause (p)", pause_game, 100)
frame.add_label(" ")
frame.add_label("Player 1")
frame.add_label("-------------------------")
frame.add_label("Paddle Up - w")
frame.add_label("Paddle Down - s")
frame.add_label(" ")
frame.add_label("Player 2")
frame.add_label("-------------------------")
frame.add_label("Paddle Up - Up Key")
frame.add_label("Paddle Down -  Down Key")
flashtimer = simplegui.create_timer(50, handle_flashtimer)


tick_sound=simplegui.load_sound(tick_sound_url) 
ball_missed_sound=simplegui.load_sound(ball_missed_sound_url)
pad_hit_sound = simplegui.load_sound(pad_hit_url)

# start frame
new_game()
frame.start()


#Rubric Grading
# 1 pt - The ball spawns in the middle of 
# the canvas with either an upward left or 
# an upward right velocity. No credit if 
# the ball moves only horizontally left or 
# right. Bleh, that would be boring!

### Checked. It moves. Random Used.

#2 pts - The ball bounces off of the top 
#and bottom walls correctly. (1 pt each)

### Checked. It does

#2 pts - The ball respawns in the middle 
#of the screen when it strikes the left 
#or right gutter but not the paddles. (1 pt
#for each side) Give credit for this item 
#even if the ball hits the edge of the 
#canvas instead of the gutter.

### Checked.

#1 pt - The left and right gutters (instead 
#of the edges of the canvas) are properly 
#used as the edges of the table.

### Checked. Yes

#1 pt - The ball spawns moving towards the 
#player that won the last point.

### Checked

#2 pts - The 'w' and 's' keys correctly control 
#the velocity of the left paddle as described 
#above. Please test each key in isolation. 
#(1 pt if the paddle moves, but in an incorrect 
# manner in response to 'w' and 's' key presses.)

### Checked - w for up. s for down. Keyup works 
### as well

#2 pts - The up and down arrows keys correctly 
#control the velocity of the right paddle as 
#described above. Please test each key in 
#isolation. (1 pt if the paddle moves, but in an 
#incorrect manner in response to up and down
#arrow key presses.)

### Checked - both keys work well 

#2 pts - The edge of each paddle is flush 
#with the gutter. (1 pt per paddle)

### This was tricky statement. works well.

#2 pts - The paddles stay on the canvas at all 
#times. (1 pt per paddle)

### Checked. Yes

#2 pts - The ball correctly bounces off the left 
#and right paddles. (1 pt per paddle)

### Oh yes. Checked

#1 pt - The scoring text is positioned and 
#updated appropriately. The positioning need 
#only approximate that in the video.

### Yes. Very well

#1 pt - The game includes a "Restart" button 
#that resets the score and relaunches the ball.

### Yes. 