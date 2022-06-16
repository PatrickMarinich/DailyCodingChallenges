#the problem (easy)

#Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

#For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

#In this example, assume nodes with the same value are the exact same node objects.

#Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


#my solution

#since the nodes with the same values are the same objects
#I will iterate throiugh the lists, keeping track of their values in an array,
#then where there is a duplicate I will then find that node and return it


#my node class
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def findIntersect(head1, head2):
    
    temp1 = head1

    #puts all of the values of list 1 into an array
    values = []
    while temp1 is not None:
        values.append(temp1.val)
        temp1 = temp1.next

    #checks the value of the node, if it matches a calue in the list return it
    while head2 is not None:
        if head2.val in values:
            return head2
        head2 = head2.next
        
       
a = Node(3, Node(7, Node(8, Node(10, None))))
b = Node(99,Node(1,Node(8,Node(10,None))))

#should print 8
print(findIntersect(a,b).val)
        

