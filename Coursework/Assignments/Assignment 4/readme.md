## Assignment 4

![Cap 1](https://github.com/jasminecronin/intro-to-cs-I/blob/master/Coursework/Assignments/Assignment%204/assignment4-1.png)

![Cap 2](https://github.com/jasminecronin/intro-to-cs-I/blob/master/Coursework/Assignments/Assignment%204/assignment4-2.png)

### Rush Hour - Text-Based Version:

	Load a game file with the following call:
		python3 RushHourGame.py game0.txt
		

	The rules for legal moves are as follows:
		1. Any horizontal car must stay in its row, and any vertical car must
			stay in its column.
		2. Any car cannot be moved to a space it is already covering.
		3. Any car cannot be moved through or onto a space occupied by another
			car. The path to the destination must be unobstructed.
		4. A destination outside of the grid cannot be selected.
			
	Moves that break one or more of the above rules will result in an error
	message, and the game will prompt for another input. User will be prompted
	until car 0 is moved to row 2, col 5.


	Inputs must be of the form: 
		a, b, c	
	Where:
		a = The integer representing the car you want to move
		b = The row coordinate of the destination (0-5)
		c = The column coordinate of the destination (0-5)	
	These numbers must be separated by commas, with or without spaces.


### Rush Hour - Graphical Version

	Load a game file with the following call:	
		python3 RushHourGUI.py game0.txt
		
		
	Rules for legal moves are exactly the same as for the text version above.
	However illegal moves will result in only the currently highlighted car
	becoming deselected. User will be allowed to make moves until the red car
	is moved to the last space in the third row.
