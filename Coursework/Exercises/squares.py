#This program opens a drawing window with a green background. It will draw squares 
#nested inside eachother in pink pen, starting with the smallest inner square.

import turtle

#Puts the pen down, draws a square with a side of length s
def draw_square(s) :
    for i in range(4) :
        turtle.forward(s)
        turtle.left(90)

#Moves the pen to the next starting position given the distance between the squares r
def reposition(r) :
    turtle.penup()
    for i in range(2) :
        turtle.right(90)
        turtle.forward(r/2) #We move half the size difference of the next square
    turtle.right(180)
    turtle.pendown()
    
#Draws the nested squares given the starting size, number of squares, and difference in side 
#length between the squares
def start_draw(k, n, d) :
    for i in range(n) :
        draw_square(k)
        reposition(d)
        k = k + d #Increases the size of the square based on the distance between them
    
wn = turtle.Screen()
wn.bgcolor("lightgreen")
turtle.pensize(3)
turtle.color("hotpink")

#Starting square is 20 units on each side, drawing 5 squares, each square is 20 units larger than the previous
start_draw(20, 5, 20)

turtle.mainloop()
