# Mirrors a given string by adding the reversed string onto it
def mirror(s) :
    new_string = s
    i = -1
    for c in s :
        new_string = new_string + s[i]
        i -= 1
    return new_string
    
# Returns a string with all instances of the specified letter removed
def remove_letter(a, s) :
    new_string = ""
    for c in s :
        if c != a :
            new_string = new_string + c
    return new_string
    

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
    
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")

    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")
