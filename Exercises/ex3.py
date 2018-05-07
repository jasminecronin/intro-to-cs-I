# Returns the cardinal direction resulting from a clockwise turn from a starting direction
def turn_clockwise(n) :
    if n == "N" :
        n = "E"
    elif n == "E" :
        n = "S"
    elif n == "S" :
        n = "W"
    elif n == "W" :
        n = "N"
    else :
        n = None
    return n
    

# Returns a grade given a percentage score
def grade(n) :
    #numerical score/mark needs to be a float
    if n >= 75.0 :
        gr = "First"
    elif 70.0 <= n < 75.0 :
        gr = "Upper Second"
    elif 60.0 <= n < 70.0 :
        gr = "Second"
    elif 50.0 <= n < 60.0 :
        gr = "Third"
    elif 45.0 <= n < 50.0 :
        gr = "F1 Supp"
    elif 40.0 <= n < 45.0 :
        gr = "F2"
    else :
        gr = "F3"
    
    return gr
    
