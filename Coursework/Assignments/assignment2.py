"""Chasing Alice is a turn-based game where the user controls a blue turtle,
Alex, to chase and catch a red turtle, Alice. The program takes w, a, s, and
d as movement inputs for Alex. The game ends when Alex comes within a certain
number of pixels of Alice.

Author: Jasmine Roebuck, Oct 23, 2017"""
    
import turtle
import random
    
def set_edges(w, h):
    """Given the height and width of the turtle canvas, returns a list
    describing the coordinates of the top, bottom, left, and right edge."""
    
    tedge = h / 2 # Top edge
    bedge = - h / 2 # Bottom edge
    ledge = - w / 2 # Left edge
    redge = w / 2 # Right edge
    edges = [tedge, bedge, ledge, redge]
    return edges


def reposition(trt, b):
    """Given a turtle object and the list of edge coordinates, repositions
    the turtle to a random location on the canvas. Leftover turtle drawings
    are cleared, and orientation remains the same."""
    
    trt.clear() # Clear previous trails
    trt.penup()
        # Randomizes location within the given border
    trt.setpos(random.randint(b[2],b[3]), random.randint(b[1],b[0]))
    trt.pendown() 
    
    
def check_position(trt, b):
    """Given a turtle object and the list of edge coordinates, checks that
    the turtle is within the border. If not, calls to reposition the turtle
    in a random location."""
    
        # If turtle is within the canvas...
    if (b[2] < trt.xcor() < b[3]) and (b[1] < trt.ycor() < b[0]):
        return # ...do nothing
    reposition(trt, b) # Otherwise, randomize location
    
    
def start_turtles(alx, alc, b):
    """Given two turtle objects and the list of edge coordinates, sets up
    the turtles in the screen with a turtle shape, red and blue colors, and
    randomizes the starting location of the red turtle."""
    
    alx.shape('turtle') 
    alx.color('blue') 
    alc.shape('turtle') 
    alc.color('red') 
    reposition(alc, b) 


def move_alice(alice, fwd, trn, b):
    """One turn for Alice. Behaviour is randomized such that 2/3 of the time,
    Alice will move forward, and 1/3 of the time she will turn either left or
    right with equal probability. Magnitudes are passed as parameters. 
    Position is validated after the move."""
    
    move = random.randint(0, 5) 
    if move == 0: 
        alice.left(trn)
    elif move == 1: 
        alice.right(trn)
    else: 
        alice.forward(fwd) 
    check_position(alice, b) # Check we are still on the canvas


def move_alex(alex, fwd, trn, inp, b):
    """One turn for Alex. A given string input of w, a, s, or d corresponds
    to a forward move, left turn, backward move, or right turn respectively.
    Magnitudes are passed as parameters. Position is validated after."""
    
    if inp == 'w':
        alex.forward(fwd) 
    elif inp == 'a':
        alex.left(trn) 
    elif inp == 'd':
        alex.right(trn) 
    elif inp == 's':
        alex.backward(fwd) 
    check_position(alex, b) # Check we are still on the canvas
    
    
def check_input(str):
    """Checks that the user input is a valid move. 'w', 'a', 's', or 'd'
    are valid moves (returns True), all others are invalid (returns False) 
    and an error is printed."""
    
    if str == 'w' or str == 'a' or str == 's' or str == 'd':
        return True
    else:
        print(str + " is not recognized as a movement. Retype.")
        return False


def get_move():
    """Gets input from the user. Calls to check the input is valid, and
    repeats prompt for input until a valid move is entered. Returns the
    validated input."""
    
    while True: # Repeat until we get a good input
        movement = input("Enter a move: ")
        if check_input(movement): 
            break
    return movement


def catch(t1, t2, d):
    """Detects the catch condition. Given two turtles, returns True once they
    are within the given distance of each other. Otherwise returns False."""
    
    if t1.distance(t2) <= d: # Check the distance between turtles
        return True
    return False


def start_stats(trt, b, d):
    """Sets up the statistics turtle. Hides the shape and moves the turtle to
    a given distance from the top left corner of the canvas."""
    
    trt.ht() 
    trt.penup() 
    trt.setpos(b[2] + d, b[0] - d) # Move to d pixels from the top left
    trt.pendown() 
    
    
def draw_stats(trt, s, d):
    """Displays the game's statistics on the canvas. Clears any previous
    stats, then rewrites with new parameters."""
    
    trt.clear() # Clear previous stats
        # Writes the step number, and distance between turtles to 2 decimals
    trt.write("Step#: {}. Distance between Alex & Alice: {:.{prec}f}.".format(
        s, d, prec = 2), font = ("ms sans Serif", 10))
    
    
def main():
    """Runs the game."""

    wn = turtle.Screen() # Create the canvas
    wnw = 500 # Canvas width
    wnh = 500 # Canvas height
    wn.setup(wnw, wnh) 
    border = set_edges(wnw, wnh) # Get the edge coordinates
  
    alex = turtle.Turtle() # Create Alex
    alex_forward = 30 # Forward/backward move distance in pixels
    alex_turn = 45 # Turn angle in degrees
    
    alice = turtle.Turtle()  # Create Alice   
    alice_forward = 20 # Forward move distance in pixels
    alice_turn = 90 # Turn angle in degrees
    
    cd = 30 # Distance required to catch Alice in pixels
    
    start_turtles(alex, alice, border) 
    
    stats = turtle.Turtle() # Create statistics turtle
    dis = 25 # Distance from the border for stat display
    step = 0 # Turn counter for stat display
    start_stats(stats, border, dis) # Position stats turtle
    draw_stats(stats, step, alex.distance(alice)) # Draw initial statistics
    
        # Play the game
    while catch(alex, alice, cd) == False : # Check catch condition
        step += 1 # Increment turn counter
            # Player moves Alex
        move_alex(alex, alex_forward, alex_turn, get_move(), border)
        draw_stats(stats, step, alex.distance(alice)) # Redraw stats
            # Check catch condition again before Alice moves
        if catch(alex, alice, cd) == True :
            break
            # Move Alice
        move_alice(alice, alice_forward, alice_turn, border)
        draw_stats(stats, step, alex.distance(alice)) # Redraw statistics
    
    wn.mainloop()


main()
