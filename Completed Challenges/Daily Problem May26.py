#Patrick Marinich

#problem

#Given an array of integers, find the first missing positive integer in linear time and constant space. 
#In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#You can modify the input array in-place.

#My solution


def getFirstMissingInt(arr):
    #first I will sort the array
    arr.sort()

    #now all of the elements should be from greatest to least, iterate through the array and see what integer is missing
    lookingfor = 1
    for i in range(len(arr)):
        if (arr[i] > 0):
            #if the element is larger then what we are looking for then return, if it is same or smaller (accounts for duplicates the check next)
            if(arr[i] != lookingfor):
                return lookingfor
            else:
                #if it is then look for the next one
                if(i != len(arr)-1):
                    #accounts for duplicates
                    if(arr[i] == lookingfor and arr[i+1] != lookingfor):
                        lookingfor += 1
                else:
                    lookingfor += 1
    return lookingfor
    
    
#tests!
print(getFirstMissingInt([3,4,-1,1])) #should be 2
print(getFirstMissingInt([1,2,0])) #should be 3
print(getFirstMissingInt([-6,-5,-1,10,17])) #should be 1
print(getFirstMissingInt([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) #should be 16
print(getFirstMissingInt([1,1,1,2,3,4])) # should be 5
print(getFirstMissingInt([-17,-51,-25,11,2,3,7,1,4,8,10,8,6,5,1,5,7,10,12,15,11,23,24])) # should be 9