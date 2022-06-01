#Problem
#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#Follow-up: Can you do this in O(N) time and constant space?


#My notes
    
# very tricky
# and example [1,4,5,9,1,3,5]  4 + 9 + 5

#compare every group of two, mark the large number, the smaller one, and the relative index of the larger. 
#after doing this then go through and check if there are sequential indecies, if there are swap the smaller of the two numbers to its small value.
#after doing these swaps, if there are still swaps then that means there was a sandwhich situation, so just remove the smaller of the numbers
#finally after giong through all of this, if there is a 2,1 pattern in the indicies, then a number was recorded twice, (ie in [2,6,4] 6 would be recorded twice
# first in index 2 and then as index 1.) Thus remove the duplicte. Once the duplicates are removed, then sum the values, and return


# complexity:
# copy | n
# compare groups of 2 | n-1
# preforming swaps | n -1
# preforming deleations n-1
# computing sum | n-M where M is number of 2,1 patterns

#overall leavinf with 5n -(3+M),  for an overall runtime of O(n) answering the follow up


#my solution

def largestSumNonAdj(currList):
    #create a copy so the origional isnt modified
    newList = currList.copy()


    #compare the list in groups of 2
    sumA = []
    sumBackup = []
    choice = []
    for i in range(len(currList)):
        #compare i and i+1;
        if( i != len(currList) - 1):
            if(currList[i] < currList[i+1]):
                sumA.append(currList[i+1])
                sumBackup.append(currList[i])
                choice.append(2)
            else:
                sumA.append(currList[i])
                sumBackup.append(currList[i+1])
                choice.append(1)
       


    #now the largest values are in A and the smaller in the backup, if
    #there are two of the same indexes next to one another then swap one
 
    for i in range(len(choice)):
        if(i != len(choice)-1):
            if(choice[i] == choice[i+1]):
                #compare and swap
                if(sumA[i] < sumA[i+1]):
                   
                    #flips sumA to sumBack
                    temp = sumA[i]
                    sumA[i] = sumBackup[i]
                    sumBackup[i] = temp
                    
                    #flips the choice
                    if choice[i] == 1:
                        choice[i] = 2
                    else:
                        choice[i] = 1

                
                else:

                     #flips sumA to sumBack, for i+1 being smaller
                    temp = sumA[i+1]
                    sumA[i+1] = sumBackup[i+1]
                    sumBackup[i+1] = temp
                    
                    #flips the choice
                    if choice[i+1] == 1:
                        choice[i+1] = 2
                    else:
                        choice[i+1] = 1


    for i in range(len(choice)):
        #check if it collides with the previous, if it does then remove the smallest
        if(i != 0):
            if(i < len(choice)):
                if(choice[i] == choice[i-1]):
                    if(sumA[i] < sumA[i-1]):
                        sumA.pop(i)
                        choice.pop(i)
                        sumBackup.pop(i)
                    else:
                        sumA.pop(i-1)
                        choice.pop(i-1)
                        sumBackup.pop(i-1)          


    #if the pattern of 2,1 is found, then remove one of the duplicates then sum
    for i in range(len(choice)):
        if(i != len(choice)-1):
            if(choice[i] == 2 and choice[i+1] == 1):
                sumA.pop(i)

    
    #finally sumA is going to be the sum that we are looking for
    total = 0
    for element in sumA:
        total += element
    return total

    

#tests!
print(largestSumNonAdj([5,1,1,5])) #expected 10,
print(largestSumNonAdj([2,4,6,2,5])) #expected 13, 
print(largestSumNonAdj([1,4,5,9,1,3,5])) #expected 18 
print(largestSumNonAdj([6,2,4,8,10,12,5])) #expected 26 
