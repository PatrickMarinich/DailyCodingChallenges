#The problem, (Medium)

#cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

#Given this implementation of cons:

#def cons(a, b):
   # def pair(f):
        #return f(a, b)
    #return pair
#Implement car and cdr.


#my notes - 
# uses inner classes, so the solution must have some type of inner class
# within it


#My solution

#defnition given
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair