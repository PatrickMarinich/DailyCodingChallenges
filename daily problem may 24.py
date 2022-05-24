#Pat Marinich
#May 24th 2022

#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?


#my soltion

#this function will return an array the same length of the input, each element in the array is the product of all of the elements in the input, but not
#including the element at the same index in the origional 
def arrProduct(arr):
    #define an output array
    output = []

    #repeat until the output is the same length of the input
    while len(output) < len(arr):
        #iterates through the input
        value = 1
        for i in range(len(arr)):
            #if i equals the current element in outout then skip, otherwise multiply
            if(i != len(output)):
                value *= arr[i]
        #append to the output
        output.append(value)

    return output


#tests!

print(arrProduct([1,2,3,4,5])) #expected [120,60,40,30,24]
print(arrProduct([3,2,1])) #expected [2,3,6]
print(arrProduct([])) #expected []
print(arrProduct([2,10,-5,-4,3])) #expected [600,120,-240,-300,400]
    
    