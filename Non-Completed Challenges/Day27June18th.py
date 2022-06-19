#The problem Easy

#Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

#For example, given the string "([])[]({})", you should return true.

#Given the string "([)]" or "((()", you should return false.


#my notes

#first attempt

#I think that a good way to check for this is to first have checks for the simple cases, such as having the same amount of open and closed of each brace.
#onces those solutions are checked for then the ordering is important.



#this function checks to see if the counts are the same for each open and close
def checkCount(input):
    if input.count('(') != input.count(')'):
        return False
    if input.count('{') != input.count('}'):
        return False
    if input.count('[') != input.count(']'):
        return False
    return True

#checks the ording of the braces, makes sure that there is nothing like ([)]
def checkOrdering(input):
    #not sure what to do here yet
    return


#tests
in1 = '(()){{}}[][]'
in2 = '((()'
print(checkCount(in1)) #expected true
print(checkCount(in2)) #expected false
