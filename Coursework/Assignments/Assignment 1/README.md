## Assignment 1: Finding Intersections with Analytic Geometry

Analytical geometry, geometry embedded in a coordinate system, is fundamental to computer graphics and physics
simulation (both key elements of video games). You will write a program that computes and displays the intersection
of a line segment with a circle. This is a simplification of a common operation in video games, i.e., casting a ray
that represents a line of sight (the line segment) to determine if an object (the circle, or sphere in three dimensions)
blocks the line of sight.

Figure 1(a) shows one way to describe a line. Two points with coordinates (x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>) define the direction
and position of the line. Given these two points, the parameter α defines the position of points along the line:

> x = (1 - α)x<sub>1</sub> + αx<sub>2</sub> (1)

> y = (1 - α)y<sub>1</sub> + αy<sub>2</sub> (2)

Note that α = 0 corresponds to (x<sub>1</sub>, y<sub>1</sub>), α = 1 corresponds to (x<sub>2</sub>, y<sub>2</sub>), 0 < α < 1, corresponds to the points between
  (x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>), and other values of alpha correspond to points on either end of the line segment.

Figure 1(b) shows the three possible situations that can arise when finding the intersection of a line with circle:
no intersection, one point of intersection when the line is tangent to the circle, and two points when the line cuts
through the circle. Let (x<sub>c</sub>, y<sub>c</sub>) be the centre of a circle with radius r. We can find if and where the intersections
occur by solving the quadratic

> αa<sup>2</sup> + bα + c = 0

where

> a = (x<sub>2</sub> - x<sub>1</sub>)<sup>2</sup> + (y<sub>2</sub> - y<sub>1</sub>)<sup>2</sup> (3)

> b = 2[(x<sub>1</sub> - x<sub>c</sub>)(x<sub>2</sub> - x<sub>1</sub>) + (y<sub>1</sub> - y<sub>c</sub>)(y<sub>2</sub> - y<sub>1</sub>)] (4)

> c = (x<sub>1</sub> - x<sub>c</sub>)<sup>2</sup> + (y<sub>1</sub> - y<sub>c</sub>)<sup>2</sup> - r<sup>2</sup>: (5)

Solutions are given by the (what should be familiar) quadratic formula:

> α = [-b ± (b<sup>2</sup> - 4ac)<sup>1/2</sup>] / 2a

When b<sup>2</sup> - 4ac < 0, α is complex and the line does not intersect the circle. When b<sup>2</sup> - 4ac = 0, there is exactly one
solution corresponding to the point where the line touches the circle tangentially. When b<sup>2</sup> - 4ac > 0, there are two
real solutions corresponding to the intersection points when the line cuts through the circle. Note that if α < 0 or
α > 1, the line intersects the circle, but not between (x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>).

### Instructions

![Figure 1](https://github.com/jasminecronin/intro-to-cs-I/blob/master/Coursework/Assignments/Assignment%201/assigment1-1.png)

Figure 1: Lines and circles: (a) two points, (x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>), define a line and the parameter α defines a position
along the line, and (b) the ways in which a line intersects (or does not intersect) a circle.

1. Read in values for x<sub>c</sub>, y<sub>c</sub>, r, x<sub>1</sub>, y<sub>1</sub>, x<sub>2</sub>, and y<sub>2</sub>. Your program should be able to read the values from the
example input files when redirected to stdin.
2. Use the turtle graphics module to display the line segment and the circle.
3. Compute the positions of the intersections between the line segment and circle, and display them if they exist.
