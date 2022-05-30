#A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#Given the root to a binary tree, count the number of unival subtrees.


#my notes:
#binary tree, all values must be 1 or zero
#all leaves will be a unival subtree
#go through and check if all children are the same


#my solution

#definitaion of a node!
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



#the main recursive function that will return the amount of unival subtrees
def UnivalCount(root):
    total = UnivalCountHelper(root,0)
    return total


#helper 1, this uses functions written below to first check if the current root is a unival tree, and if so then count all of the nodes,
# as combinotrically if a sub tree is uninval, then it contains N univals trees where N is the number of nodes
def UnivalCountHelper(root,total):
    if (UnivalCheck(root,root.val) == True):
        #count all of the roots here, and accumliate
        total += NodeCount(root,0)
    else:
        if(root.left is not None):
           total =  UnivalCountHelper(root.left,total)
        if(root.right is not None):
            total = UnivalCountHelper(root.right,total)
    
    return total

    
    
    

#checks if the current subtree is unival
def UnivalCheck(root,rootValue):
   #check if every value in this tree is the same, if it is, count the nodes and that is how many sub trees there are
    if(root.left is None and root.right is None):
        if(root.val == rootValue):
            return True
        else: 
            return False
    else:
        #if the right node exists
        if(root.right is not None):
            if(root.val == rootValue):
                #if the vales match, then recursive call
                return UnivalCheck(root.right,rootValue)
            else:
                return False
        #do the same for the left
        if(root.left is not None):
            if(root.val == rootValue):
                return UnivalCheck(root.left,rootValue)
            else:
                return False

#coutns the amount of nodes in a given tree
def NodeCount(root,count):
    #if there are no children, increment the count and return
    if(root.left is None and root.right is None):
        count += 1
        return count
    else:
        #if not increment the count and then call on children
        count += 1
        if(root.left is not None):
            count =  NodeCount(root.left,count)
        if(root.right is not None):
            count = NodeCount(root.right,count)
    return count

  
    





#tests below
# the root A generated below will look like
#           1
#         /  \
#         1   1
#        / \  / \  
#       1  1  1 1

#this contains 7

#root b
#       1
#      / \
#     1   0
#contains 2

# the root C generated below will look like
#           1
#         /  \
#         1   1
#        / \  / \  
#       1  1  1 0
#contains 5

#tree declarations
rootA = Node(1, Node(1, Node(1,None,None), Node(1,None,None)), Node(1, Node(1,None,None),Node(1,None,None)))
rootB = Node(1, Node(1, Node(1,None,None), Node(0,None,None)))
rootC = Node(1, Node(1, Node(1,None,None), Node(1,None,None)), Node(1, Node(1,None,None),Node(0,None,None)))

#helper method checks
a = UnivalCheck(rootA,rootA.val)
b = UnivalCheck(rootB,rootB.val)
c = UnivalCheck(rootC,rootC.val)
print(a) #expected true
print(b) #expected false
print(c) #expected false


#final tests
print(UnivalCount(rootA)) #expected 7
print(UnivalCount(rootB)) #expected 2
print(UnivalCount(rootC)) #expected 5