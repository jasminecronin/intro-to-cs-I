"""Assignment 4: The Object of the Game
This program plays a text based version of the game Rush Hour. Moves are 
prompted to the console and entered by the user. The game grid is printed
after every move. See the rules for legal moves in the readme.txt file.

Author: Jasmine Roebuck, Nov. 27, 2017"""

import sys

def main():
    """Runs the game."""
    
    lst = loadGame() # Load the game file
    gameState = Grid() # Create the game grid
    for row in range(len(lst)):
        gameState.addCar(lst[row]) # Add each car to the grid
    
    # Game loop
    while gameState.win() == False: # Win condition
        print(gameState) # Print the game board
        move = get_move() # Get the move from the player
        if gameState.check(move) != True: # Make sure the move is valid
            print("Invalid move, please retype.)
            continue # Prompt again if we get an invalid move
        gameState.moveCar(move) # Process the move
    

class Car:
    """Creates a car object given a list of attributes. They are:
    orientation, length, row coordinate, and column coordinate.
    The latter 3 must be converted from strings to ints.
    Coordinates refer to the upper left corner of the car."""
    
    def __init__(self, attr):
        """Initializes car attributes to the given values."""
        self.orient = attr[0] # 'h' or 'v'
        self.len = int(attr[1]) # 2 or 3
        self.row = int(attr[2]) # 0-5
        self.col = int(attr[3]) # 0-5  
    
    
class Grid:
    """Creates and manages the game grid represented by a 2-dimensional list.
    Contains a list of all car objects, checks and performs car moves."""
    
    def __init__(self):
        """Initiates the game grid as a 2-dimensional list. Fills the grid
        with '.' (referring to an empty space). Creates an empty list to
        contain all car objects that will be added."""
        
        self.grid = []
        for i in range(6): # Grid is a 6x6 square
            row = ['.', '.', '.', '.', '.', '.']
            self.grid.append(row)  
        self.allCars = [] # Start an empty list for the car objects
        
        
    def __str__(self):
        """Formats the game grid into a printable string to ba called with
        a print statement."""
        
        state = '' # Start with an empty string
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == '.': # If the space is empty
                    state += '  .' # Print a period
                else: # Space is occupied, print the car's number
                    state += '{:3}'.format(self.grid[row][col])
            state += "\n" # Add a newline at the end of each row
        return state # Return the string
        
        
    def addCar(self, attr):
        """Given a list of car attributes, creates a car object containing
        those attributes. Adds the car to the total list of cars. Draws the
        car in the game grid."""
        
        car = Car(attr) # Create the car
        self.allCars.append(car) # Maintain a list of the car objects
        self.drawCar(car) # Draw the car in the grid
                
                
    def win(self):
        """Checks if the grid has met the win condition. For the game to end,
        the player's car (car 0) must be covering the last space in row 2."""
        
        if self.grid[2][5] == 0:
            return True
        return False
        
        
    def check(self, move):
        """Validates the tuple representing the user's move choice. Returns
        True if the move doesn't break rules, returns False if it does."""
        
        (carnum, row, col) = move # Unpack the tuple
        
        # Check the selected car is an available one on the board.
        if carnum < 0 or carnum >= len(self.allCars):
            return False
            
        # Check the target space is inside the game board.
        if row < 0 or row > 5 or col < 0 or col > 5:
            return False
        
        car = self.allCars[carnum] # Grab the car object we want to move
        
        # First deal with the case of a horizontal car
        if car.orient == 'h' and car.row == row: # Keep car in same row
            if col < car.col: # If we are moving to the left
                for i in range( car.col - col ): # Check from car to target
                    if self.grid[row][col + i] != '.': # Check path is clear
                        return False # Path is obstructed
                return True
            elif col >= (car.col + car.len): # Moving to right, car must
                                                #   not already be on target
                # Similar to above, check spaces between car and target
                for i in range(col - (car.col + car.len) + 1):
                    if self.grid[row][car.col + car.len + i] != '.':
                        return False # Path is obstructed
                return True
                
        # Now deal with the case of a vertical car
        elif car.orient == 'v' and car.col == col: # Keep car in same col
            if row < car.row: # Moving up
                for i in range(car.row - row): # Check from car to target
                    if self.grid[row + i][col] != '.': # Check path is clear
                        return False # Path is obstructed
                return True
            elif row >= (car.row + car.len): # Moving down, car must not
                                                # already be on target
                # Similar to above, check spaces between car and target
                for i in range(row - (car.row + car.len) + 1):
                    if self.grid[car.row + car.len + i][col] != '.' :
                        return False # Path is obstructed
                return True
                
        # If we get here, either car was not kept in same row/col, or the car
        #   already occupies the target space
        return False 
        
        
    def moveCar(self, move):
        """Given a valid move tuple, erases the car from the grid, updates
        the car object's position attributes, and redraws the car."""
        
        (carnum, row, col) = move # Unpack the tuple
        car = self.allCars[carnum] # Grab the car object
        self.eraseCar(car) # First erase the car
        if car.orient == 'h': # Car is horizontal
            if col < car.col: # Moving left
                car.col = col
            else: # Moving right
                car.col = col - (car.len - 1)
        else: # Car is vertical
            if row < car.row: # Moving up
                car.row = row
            else: # Moving down
                car.row = row - (car.len - 1)
        self.drawCar(car) # Redraw the car in the grid
                
          
    def eraseCar(self, car):
        """Given a car object, erases the car from the game grid, replacing
        its number representation with periods."""
        
        if car.orient == 'h': # Car is horizontal
            for i in range(car.len): # 2 or 3 spaces
                self.grid[car.row][car.col + i] = '.' # Erase
        else: # Car is vertical
            for i in range(car.len): # 2 or 3 spaces
                self.grid[car.row + i][car.col] = '.' # Erase
        
        
    def drawCar(self, car):
        """Draws the given car object in the game grid. Car is represented
        by its number in the allCars list, starting from 0."""
        
        for i in range(car.len): # For 2 or 3 squares
            if car.orient == 'h': # Draw the car across the row
                self.grid[car.row][car.col + i] = self.allCars.index(car)
            else: # Draw the car down the column
                self.grid[car.row + i][car.col] = self.allCars.index(car)
        

def loadGame():
    """Translates the game text file into a workable list in order to set up
    the game grid. Returns a 2-dimensional list containing all initial game
    state information: rows refer to individual cars, columns are the 
    orientation, length, and position of each car."""
    
    gamefile = sys.argv[1]
    game = open(gamefile, 'r')
    cars = [] 
    for line in game.readlines():
        cars.append(line.strip().split(", ")) # Strip commas, whitespace
    game.close() 
    return cars


def get_move():
    """Prompt the user for input and convert the input into a tuple to be
    used by the Grid class."""
    
    move = input("Enter a move (car number, row, column): ")
    move = move.replace(' ', '')
    move = move.split(',')
    set = (int(move[0]), int(move[1]), int(move[2]))
    return set
        
        
if __name__ == '__main__':
    main()
