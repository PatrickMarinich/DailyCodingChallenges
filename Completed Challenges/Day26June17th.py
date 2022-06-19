#The Problem Medium

#Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

#The list is very long, so making more than one pass is prohibitively expensive.

#Do this in constant space and in one pass.


#my idea
#attempt one
#since it is a single linked list, my idea is to check k+1 nodes away from the current node. if the k+1th node away is set to null, then that must be the kth 
#last from the end of the list. then it will also be easy to remove as just sent node.next == node.next.next

#node class
class node:
    def __init__(self,data,next):
        self.data = data
        self.next = next


#the plan is to check the node k away, if its next is null, then head.next is the one to remove. 
#I am allowed to igner the cause of k=len(list) as it says that in the problem
#k will also never be too big due to this sitpulation so I do not have to check for it
def removeKth(head,k):

    #make a shallow copy so that I can recusive call if nessassary
    headcopy = head
    
    #iterate k nodes away
    for i in range(k):
        headcopy = headcopy.next

    #if true then remove the next node 
    if(headcopy.next is None):
        head.next = head.next.next
        return
    else:
        #if not then just recursive call
        removeKth(head.next,k)


#for testing, prints all the values
def printall(head):
    print("starting list:")
    while(head is not None):
        print(head.data)
        head = head.next


#tests
# 3 -> 4 -> 5 -> 6 -> 7 -> null
list1 = node(3,node(4,node(5,node(6,node(7,None)))))

printall(list1) 
removeKth(list1,2) #removes 6
printall(list1)

        



