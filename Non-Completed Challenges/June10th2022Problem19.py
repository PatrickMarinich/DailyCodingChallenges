#The Problem (medium)

#A builder is looking to build a row of N houses that can be of K different colors. 
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

#Given an N by K matrix where the nth row and kth column 
# represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.


#notes:
#Houses are in the rows, where as the columns are the colors

#so the goal will be to find a path through the matrix, where neighboring entires are non-existant, but is also the minimim

#exmaple

#  1  1  1  0
#  3  2  1  0
#  2  1  0  2
#  3  2  1  1

# the solution would be 0 from col 1, 1 from col 2, 0 from col 3 and 1 from col 4





