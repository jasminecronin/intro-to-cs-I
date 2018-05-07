class Rectangle:
    def __init__(self, posn, w, h) :
        self.corner = posn
        self.width = w
        self.height = h
        
    def __str__(self) :
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)
        
    def perimeter(self) :
        p = (2*self.width) + (2*self.height)
        return p
        
    def flip(self) :
        temp = self.width
        self.width = self.height
        self.height = temp
        
class Point :
    def __init__(self, x=0, y=0) :
        self.x = x
        self.y = y
    
    
if __name__ == '__main__' :
    import sys

    def test(did_pass):
        """ Print the result of a test. """
        linenum = sys._getframe(1).f_lineno # Get the caller's line number.
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at the line {0} FAILED.".format(linenum))
        print(msg)
    
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.perimeter() == 30)
    
    r = Rectangle(Point(100, 50), 10, 5)
    test(r.width == 10 and r.height == 5)
    r.flip()
    test(r.width == 5 and r.height == 10)
