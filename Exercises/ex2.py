#This function returns the area of a circle given the radius r.

def area_of_circle(r) :
    pi = 3.14159 #This can be imported from the math module,
                 #but I chose to approximate it here because I 
                 #wanted to keep the functionality encapsulated
                 #within the function.
    
    area = pi*(r**2)
    return area
