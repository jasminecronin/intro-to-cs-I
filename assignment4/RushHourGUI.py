"""This is a graphical version of the Rush Hour game defined in 
RushHourGame.py. See the rules for operation in the readme.txt.

Author: Jasmine Roebuck, Nov. 27, 2017"""

import RushHourGame, pygame
            
def main():
    """Runs the graphical game."""
    
    pygame.init()
    
    board = RushHourGame.Grid() # Initialize the game board
    gamelist = RushHourGame.loadGame() # Load the game file
    
    Game = GUI(board, gamelist) # Initialize the GUI
    gameOver = False # Loop condition
    
    while gameOver == False: # Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Presses the exit button
                gameOver = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos() # Get mouse position
                Game.move(x, y, board) # Process the mouse input
                gameOver = board.win() # Check if we've won
                

class GUI:
    """Runs and maintains the graphical representation of the game overtop
    of the text version. Translates mouse positions into board moves, and
    draws and erases cars on the board as required."""
    
    def __init__(self, board, gamelist):
        """Initialize the GUI object given a 2D game state list and the 
        loaded game."""
        
        self.width = 600 # Width of the game window
        self.height = 600 # Height of the game window
        self.cell = 100 # Size of each cell in the 6x6 game grid
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.lightgreen = (200, 255, 200)
        self.bg = (70, 70, 70) # Background color
        
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.screen.fill(self.bg) # Fill with background color
        self.active = None # The currently active car object
        
        for row in range(len(gamelist)):
            board.addCar(gamelist[row]) # Add each car to the board
        self.carlist = board.allCars # Get the list of car objects
        for car in self.carlist: # Draw each car on the board
            if self.carlist.index(car) == 0:
                self.draw_car(car, self.red) # First car is red
            else:
                self.draw_car(car, self.green) # Rest are green
        pygame.display.flip()
        
    
    def draw_car(self, car, color):
        """Given a car object and a color, draw a rectangle on the canvas
        to represent it."""
        
        carx = (car.row * self.cell) + 5 # x-coord +5 pixels of padding
        cary = (car.col * self.cell) + 5 # y-coord +5 pixels of padding
        if car.orient == 'h': # If car is horizontal
            cw = (car.len * self.cell) - 10 # Width len*cell size - padding
            ch = self.cell - 10 # Height is cell size minus padding
        else: # Car is vertical
            cw = self.cell - 10 # Similar to above, account for padding
            ch = (car.len * self.cell) - 10
            
        rectangle = (cary, carx, cw, ch) # Define the rectangle to draw
        pygame.draw.rect(self.screen, color, rectangle)
        
        
    def pick_color(self, car):
        """Chooses which color to draw the car, red or green, based on if the
        first car is being redrawn or not. Car must be the integer number."""
        
        if car == 0:
            return self.red
        else:
            return self.green
        
        
    def move(self, x, y, board):
        """Given the mouse click coordinates and the list representation of
        the game, process the move."""
        
        row = y // self.cell # Get the car's row
        col = x // self.cell # Get the car's column
        
        if board.grid[row][col] != '.': # Clicked occupied space
            if self.active != None: # Already have an active car
                # Redraw the active car in original color
                self.draw_car(self.carlist[self.active], self.pick_color(self.active))
                pygame.display.flip()
            # Make the clicked on car the active car
            self.active = board.grid[row][col]
            self.draw_car(self.carlist[self.active], self.lightgreen) # Highlight it
            pygame.display.flip()
            
        else: # Clicked on empty space
            if self.active != None: # Already have an active car
                movelist = (self.active, row, col) # Tuple to pass to validation function
                if board.check(movelist): # If the move is allowed
                    self.draw_car(self.carlist[self.active], self.bg) # Erase the car
                    board.moveCar(movelist) # Process the move, redraw car
                    self.draw_car(self.carlist[self.active], self.pick_color(self.active))
                    pygame.display.flip()
                else: # Move is not allowed, redraw car in original color
                    self.draw_car(self.carlist[self.active], self.pick_color(self.active))
                    active = None # Reset the active car
                    pygame.display.flip()
            # else: We don't have an active car and clicked on empty space, so do nothing
    
 
main()
