#This program uses turtle graphics to draw a 5-pointed star.

import turtle

star = turtle.Turtle() #The turtle object

angle = 144 #Angle in degrees for each turn
sides = 5 #Number of sides of the shape
length = 150 #Length of each side of the shape in pixels

star.pensize(3) 

for i in range(sides) : #For each side of the shape
    star.forward(length) #Draw a side
    star.right(angle) #Turn the turtle
    
turtle.mainloop()
