#The Problem (Easy)

#Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

#For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

#my idea
#get the overall start and end times, and then go through each number and see if there is any overlap between them. If there is then increment
#a counter, and return the highest number



#the input will be an array of arrays size 2, where the first number is the start time and the last number is the end time

def minClassrooms(input):

    startTimes = []
    endTimes = []

    for times in input:
        startTimes.append(times[0])
        endTimes.append(times[1])

    #gets the overall start and end times
    overallStart = min(startTimes)
    overallEnd = max(endTimes)

    maxCount = 1
    #goes through each possible time
    for  overallStart in range(overallEnd):
        count = 0
        #if a class is at the current time then count it
        for times in input:
            if overallStart >= times[0] and overallStart <= times[1]:
                count = count + 1
        #if the count is larger then the most, then make it the new max
        if count > maxCount:
            maxCount = count

    return maxCount





#tests
a = [[30,75], [0,50], [60,150]]
b = [[0,12], [2,20], [3,30], [4,40]] 
c = [[20,30],[40,50],[60,70]]
d = [[10,20]]
print(minClassrooms(a)) #expected 2
print(minClassrooms(b)) #expected 4
print(minClassrooms(c)) #expected 1
print(minClassrooms(d)) #expected 1