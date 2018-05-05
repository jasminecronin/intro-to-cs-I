"""Assignment 3: AI Training
This program plays a game of nuts. There are a number of nuts on a table, and
two players take turns picking up 1-3 nuts. The player to pick up the last nut
loses. This game can be played with 2 human players, one player against an
untrained AI, or one player against a trained AI.

Author: Jasmine Roebuck, November 6, 2017"""

import random

def main():
    """Main module. Prints the menu and calls the game choice."""
    
    print("Welcome to the game of nuts!")

    nuts = start_nuts() #Prompt for initial number of nuts
    
    print("Options:") # Print out the options menu
    print(" Play against a friend (1)")
    print(" Play against the computer (2)")
    print(" Play against the trained computer (3)")
    
    # Get the player's option choice
    opt = int(input("Which option do you take (1-3)? "))
    while opt < 1 or opt > 3:
        opt = int(input("Invalid input. Please enter a number from 1 to 3 "))
    
    # Run the appropriate game
    if opt == 1:
        option1(nuts)
    elif opt == 2:
        option2(nuts)
    elif opt == 3:
        option3(nuts)
        
        
def option1(n) :
    """Runs a human v. human game. Takes in the inital number of nuts. Prints
    out game statuses."""
    
    player = 1 
    while True: # Continue until there are < 1 nuts on the board
        print("\nThere are ", n, " nuts on the board.")
        pickup = player_nuts(player) # Get the player's pickup choice
        n -= pickup
        if n < 1: 
            print("Player {}, you lose.".format(player))
            break
        if player == 1: # Swap the current player to the opposite player
            player = 2
        else :
            player = 1


def option2(n):
    """Runs human v. AI games. Can play multiple games. The AI makes its choices
    randomly, and it will build a probability table of optimal choices as it plays
    more games."""
    
    # Initializes probability table. Each row in the table corresponds to 
    # the number of nuts currently in the game.
    hats = create_table(n) 
    play_again = 1
    initial_nuts = n # Remember starting nut count

    while play_again != 0: # Play games until player enters 0
        human_v_ai(hats, n) # Run a human v. AI game
        n = initial_nuts # Reset the nut counter
        # Prints the probability table after winning/losing. Uncomment these lines to view.
        # Note that hats[0] is unused, hats[row][0] is used for tracking winning moves.
        # print()
        # print( hats )
        play_again = int(input("Play again (1 = yes, 0 = no)? "))
        

def option3(n):
    """Trains the AI, then runs human v. AI games. Option for multiple games.
    Builds probability tables for 2 AIs. The first AI achieves far more wins
    than the second AI, so AI1 is then used as the opponent for the player."""
    
    ai1 = create_table(n) # Initialize the probability tables
    ai2 = create_table(n)
    play_again = 1
    initial_nuts = n # Remember starting nut count
    training_sessions = 100000 # Number of AI v AI games to run
    
    print("Training AI, please wait...")
    for i in range(training_sessions): 
        ai_v_ai(ai1, ai2, n)   
        
    # Note that ai1[0] and ai2[0] are unused, ai[row][0] is used for tracking winning moves.
    # print()
    # print(ai1)
    # print(ai2)
    
    while play_again != 0: # Play games until player enters 0
        human_v_ai(ai1, n) # Run a human v. AI game
        n = initial_nuts # Reset the nut counter
        play_again = int(input("Play again (1 = yes, 0 = no)? "))
    
    
def human_v_ai(hats, n):
    """Runs a single human v. AI game given the probability table for the AI
    and the initial nut number. Prompts the user for pickup choice, directs 
    the AI to make its selection randomly."""
    
    player = 1 # Start with the human player
    while True: # Continue until there are < 1 nuts on the board
        print("\nThere are ", n, " nuts on the board.")
        if player == 1:
            pickup = player_nuts(player) # Get the player's move
            n -= pickup # Reduce the nuts on the table
            player = 2 # Swap to AI
        else: 
            pickup = ai_nuts(hats, n, True) # Get the AI's move
            n -= pickup # Reduce the nuts on the table
            player = 1 # Swap to player
        if n < 1: 
            if player == 1: # Last move was the AI's
                print("AI loses.")
                win = False # AI lost
            else: # Last move was player's
                print("You lose.")
                win = True # AI won
            adjust_table(hats, win) # Adjust the probabilities in the table
            break
            
       
def ai_v_ai(ai1, ai2, n):
    """Runs a single AI v. AI game given two probability tables and the initial
    number of nuts on the board. Directs both AIs to choose their moves
    randomly using the weights in their respective tables."""
    
    player = 2 # Start with the second AI
    win1 = False
    win2 = False
    while True: # Continue until there are < 1 nuts on the board
        if player == 1:
            pickup = ai_nuts(ai1, n, False) # Make move choice
            n -= pickup # Reduce nuts on the board
            player = 2 # Swap to AI 2
        else: 
            pickup = ai_nuts(ai2, n, False) # Make move choice
            n -= pickup # Reduce nuts on the board
            player = 1 # Swap to AI 1
        if n < 1:
            if player == 1 : # AI 2 made final move
                win1 = True
            else : # AI 1 made final move
                win2 = True
            adjust_table(ai1, win1) # Adjust probabilities in both tables
            adjust_table(ai2, win2)
            break
        

def start_nuts():
    """Gets the initial number of nuts from the player. Must be an integer
    between 10 and 100. Non-integer inputs are invalid. Returns the number
    to the main module."""
    
    num = int(input("How many nuts are there on the table initially (10-100)? "))
    while num < 10 or num > 100: 
        print("Please enter a number between 10 and 100.")
        num = int(input("How many nuts are there on the table initially (10-100)? "))
    return num
    
    
def player_nuts(p):
    """Gets and returns the player's choice of the number of nuts to pick up.
    must be an integer between 1 and 3 inclusive. Non-integer inputs are
    invalid."""
    
    num = int(input("Player {}: How many nuts do you take (1-3)? ".format(p)))
    while num < 1 or num > 3:
        print("Please enter a number between 1 and 3.")
        num = int(input("Player {}: How many nuts do you take (1-3)? ".format(p)))
    return num
                

def ai_nuts(hats, row, player):
    """Determines and returns the AI's pickup choice given the AI's probability
    table and number of nuts currently on the board. Prints status messages
    only if the opposing player is human."""
    
    i = [1, 2, 3] # List of the available move choices
    # Randomizes based on the current weights in the probability table
    pick = random.choices(i, weights=hats[row][1:])
    hats[row][0] = pick[0] # Record the move choice
    if player == True: # If we have a human player
        print("AI selects ", pick[0]) # Tell what the AI chose
    return pick[0] 
    

def create_table(n):
    """Initializes a probability table for the AI given the initial number of
    nuts. Creates n + 1 rows such that the row index refers directly to the
    current number of nuts (the first row is unused). Each row contains a sublist
    with index 1, 2, and 3 referring to the nut pickup choice. Index 0 is used for
    tracking winning moves."""
    
    table = []
    for i in range(n + 1):
        row = [0, 1, 1, 1]
        table.append(row)
    return table
    
   
def adjust_table(h, win):
    """Adjusts the probability of the given table depending on if the AI
    won or lost."""
    
    for row in range(len(h)): # Go through the whole table
        pick = h[row][0] # Look at the move choice
        if pick != 0: # Only adjust if the AI made a move
            if win == True: # If the AI won
                h[row][pick] += 1 # Increase the probability of this move
            elif win == False and h[row][pick] > 1: # If AI lost
                h[row][pick] -= 1 # Decrease the probability (can't go below 1)
            h[row][0] = 0 # Erase the stored move
    
    
main()
