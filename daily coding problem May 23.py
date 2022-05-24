#Patrick Marinich
# daily coding problem May 23
#The Problem:

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: can you do it in one array pass?

#My Solution is below and I believe it has a Run Time of (n + n-1 + n-2 + n-3 ...... 0) = (Mn-c) where M is the list length, and c is a constant. 
#O(n)

def checkSum(input,sum):
    #makes a copy since params are pass by reference in python
    listCopy = input.copy()
    ans = 'False'

    #goes through the list and compares the first number to each other number, then the first element is popped, so that
    #no sums are calculated twice. 
    while listCopy != [] and ans != True:
        for i in range(len(listCopy)-1):
            if(i != 0):
                if(listCopy[0] + listCopy[i] == sum):
                    ans = 'True'
                
        listCopy.pop(0)

    return ans



# main method for testing
print('Input 1: 1,2,3,4,5')
input = [1,2,3,4,5]
print(checkSum(input,12)) #should be false
print(checkSum(input,6)) # should be true
print(checkSum(input,0)) #should be false
print(checkSum(input,7)) # should be true


print('Input 2: 0,-5,-1,2,-8,4')
input2 = [0,-5,-1,2,-8,4]
print(checkSum(input2,12)) #should be false
print(checkSum(input2,-6)) # should be true
print(checkSum(input2,0)) #should be false
print(checkSum(input2,-13)) # should be true


