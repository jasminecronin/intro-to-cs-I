import math

# two Points as parameters instead of four numbers
def distance( p1, p2 ) :
    return math.sqrt( (p2.x-p1.x)**2 + (p2.y-p1.y)**2 )
    
class Point :
    def __init__(self, x=0, y=0) :
        self.x = x
        self.y = y
        
    def reflect_x(self) :
        return Point( self.x, -self.y )
