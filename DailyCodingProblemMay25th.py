#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
#and deserialize(s), which deserializes the string back into the tree.

#For example, given the following Node class




class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#The following test should pass:
#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'


#my solution

#searlize - gets the values of the nodes in a recursive formatt, and append the direction "L" or "R" in front so that
# the overall direction can be accessed later

#desearlize - uses those values and directions to create new nodes and inserts them back into a binary tree.

def serialize(root):
    answer = " "
    answer = serializehelper(root,answer,None)
    return answer

def serializehelper(root,instring,direction):

    #if the root is null the return the current string
    if root is None:
        return instring
    else:
        #if the root is not null, then append the value, and recursive call on left and right
        #introduces a notifier if the string came from the left or right
        if direction == "L":
            instring = instring + " L " + root.val
        elif direction == "R":
            instring = instring + " R " + root.val
        else:
            instring = instring + " " + root.val
        string1 = serializehelper(root.left,instring,"L")
        string2 = serializehelper(root.right,string1,"R")
        return string2
    
    

def deserialize(instring):
    #given a string, split it into an array of values
    nodes = instring.split()

    #create a root node from the first value in the lsit
    currValue = nodes.pop(0)
    root = Node(currValue)
    
    #array for directions array for nodes
    arrD = []
    arrN = []

    for i in range(len(nodes)):
        if( i  % 2 == 0):
            arrD.append(nodes[i])
        else:
            arrN.append(nodes[i])


    #for each value left in this array, create a new node and insert it into the tree
    for i in range(len(arrN)):
        node = Node(arrN[i])
        insert(root,arrN[i],arrD,i)
    #return the root
    return root

#a helper function to allow for the insert of a node into a binary tree
def insert(root,value,dir,i):
    #only does less that or equat too as a perfect binary tree does not have repeat values

    #if the values is less insert to the left
    if(dir[i] == "L"):
        #if the root.left is null then create a new node and insert
        if(root.left is None):
            root.left = Node(value)
        else:
            #if its not make the root that node and call again, with the direction of previous node
            insert(root.left,value,dir,i-1)
    elif(dir[i] == "R"):
        #if root.right is null, insert value
        if(root.right is None):
            root.right = Node(value)
        else:
            #if not recursive call and try again
            insert(root.right,value,dir,i-1)



    

#tests!

#defines a binary tree
node = Node('root', Node('left', Node('left.left')), Node('right'))

#prints my serial
print(serialize(node))

#if this passes then we are good to go!
assert deserialize(serialize(node)).left.left.val == 'left.left'
print("Test Passed!")
