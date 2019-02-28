# Chapter 18, exercise 7

# put the function 'flatten' in this file

# Write a function 'flatten' that returns a simple list containing all the
# values in a nested list.

def flatten( n_list ) :
    l = []
    
    for i in n_list :
        if type(i) == type([]) :
            l.extend(flatten(i))
        else :
            l.append(i)
    
    return l

        
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
    
    test(flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6])
    test(flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6])
    test(flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6])
    test(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==
                  ["this","a","thing","a","is","a","easy"])
    test(flatten([]) == [])
