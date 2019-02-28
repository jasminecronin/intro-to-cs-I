# Replaces a string of characters with a new string of characters
def replace( s, old, new ) :
    #split the string up, using the old string as the delimiter
    new_string = ""
    list = s.split( old )
    new_string = new.join(list)
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
    
    test( replace("Mississippi", "i", "I" ) == "MIssIssIppI" )
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test( replace( s, "om", "am" ) == "I love spam! Spam is my favorite food. Spam, spam, yum!" )
    test( replace( s, "o", "a" ) == "I lave spam! Spam is my favarite faad. Spam, spam, yum!" )
