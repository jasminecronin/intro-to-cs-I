"""This program will read in data from a file for the centre point and radius
of a circle, and two points to form a line segment. It will then draw the 
circle and line segment. If the line segment intersects the circle, the 
intersection point(s) will be computed and displayed with a small black dot.

Author: Jasmine Roebuck"""

import turtle
import math


def draw_line(x1, y1, x2, y2):
    """Draws a line segment given the coordinates of two points. Circles
    the endpoints of the segment."""
    draw_circle(x1, y1, 4) #Circles the endpoint with a radius of 4
    turtle.penup()
    turtle.setpos(x1, y1)
    turtle.pendown()
    turtle.setpos(x2, y2)
    draw_circle(x2, y2, 4)
    

def draw_circle(xc, yc, r):
    """Draws a circle given the coordinates of the center and the radius"""
    turtle.penup() 
    turtle.setpos(xc, (yc - r))
    turtle.pendown() 
    turtle.circle(r)


def calc_a(x1, y1, x2, y2):
    """Calculates the first coefficient for the quadratic formula."""
    a = (((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return a


def calc_b(xc, yc, x1, y1, x2, y2):
    """Calculates the second coefficient for the quadratic formula."""
    b = 2 * ((x1 - xc) * (x2 - x1) + (y1 - yc) * (y2 - y1))
    return b


def calc_c(xc, yc, r, x1, y1):
    """Calculate the third coefficient for the quadratic formula."""
    c = ((x1 - xc) ** 2) + ((y1 - yc) ** 2) - (r ** 2)
    return c


def determinant(a, b, c):
    """Calculates the determinant of the quadratic formula. This tells us 
    how many intersections we have, assuming infinite length lines."""
    det = (b ** 2) - (4 * a * c)
    return det


def sol_num(a, b, c):
    """Calculates the number of solutions we have, assuming lines
    of infinite length."""
    det = determinant(a, b, c)
    if det < 0:
        return 0
    elif det == 0:
        return 1
    else:
        return 2


def alpha_zero(a, b, c):
    """Calculates alpha when we have only one intersection."""
    alpha = (-b / ( 2 * a ))
    return alpha


def alpha_pos(a, b, c):
    """Calculates the first alpha when we have two intersections."""
    alpha = (-b + math.sqrt(determinant(a, b, c))) / (2 * a)
    return alpha


def alpha_neg(a, b, c):
    """Calculates the second alpha when we have two intersections."""
    alpha = (-b - math.sqrt(determinant(a, b, c))) / (2 * a)
    return alpha


def segm_intsct(alpha):
    """Determines if the given alpha will return a solution that lies inside
    our line segment."""
    if 0 <= alpha <= 1 : #The intersection point will be on our segment
        return True
    return False


def intersect(p1, p2, alpha):
    """Returns either the x or y coordinate of an intersection point. For x,
    pass in x1 and x2. For y, pass in y1 and y2."""
    p = ((1 - alpha) * p1) + (alpha * p2)
    return p


#Set up
wn = turtle.Screen()
wn.setworldcoordinates(0, 0, 800, 800)
turtle.ht() #Hide the turtle arrow

#Get the input from a file
xc, yc = eval(input())
r = eval(input())
x1, y1 = eval(input())
x2, y2 = eval(input())

#Draw the circle and the line segment
draw_circle(xc, yc, r)
draw_line(x1, y1, x2, y2)

#Calculate the coefficients for our quadratic formula
A = calc_a(x1, y1, x2, y2)
B = calc_b(xc, yc, x1, y1, x2, y2)
C = calc_c(xc, yc, r, x1, y1)

#Determine how many solutions we have
solns = sol_num(A, B, C)

#Find the intersections
turtle.pensize(5) 
if solns == 1:
    alp1 = alpha_zero(A, B, C) #Calculate alpha
    if segm_intsct(alp1): #Check if alpha is on the segment
        x3 = intersect(x1, x2, alp1) #Get the point of intersection
        y3 = intersect(y1, y2, alp1)
        draw_circle(x3, y3, 2) #Indicate the intersection
elif solns == 2:
    alp1 = alpha_pos(A, B, C) #Calculate two different alphas
    alp2 = alpha_neg(A, B, C)
    if segm_intsct(alp1): #If alpha is on the segment
        x3 = intersect(x1, x2, alp1) #Get the point of intersection
        y3 = intersect(y1, y2, alp1)
        draw_circle(x3, y3, 2) #Indicate the intersection
    if segm_intsct(alp2) : #Repeat for the second alpha
        x4 = intersect(x1, x2, alp2)
        y4 = intersect(y1, y2, alp2)
        draw_circle(x4, y4, 2)
    

turtle.mainloop()
