#The Problem (Medium)
#The area of a circle is defined as πr^2. 
#Estimate π to 3 decimal places using a Monte Carlo method.

#Hint: The basic equation of a circle is x2 + y2 = r2.


#Notes

#The Mathmatical approach to this problem is pretty cool
#Imagine a circle with a radius of 1. if r = 1 then the area of the
#circle would be equal to exactly pi units^2
#now image that circle in inscribed a square with side length = 2
# the area of that square would be 4 unit^2

#now if you randomly select a point within the square, the ratio of
# points that land inside the circle compared to those that land
#outside the circle can be used to find pi

# pi = 4*points in the circle / total points

#this function will simulate pi using n random points,
#the larger the n, the more accurate the output

import random
def simulatePi(n):
    #initalizes the counters
    circleCount = 0
    #repeat n times where n is the input
    for i in range(n):
        #generated 2 random numbers between -1 and 1 to act
        #as points on a cordinate plane
        x = ((random.random()) * 2) -1
        y = ((random.random())*2) -1
        
        #if x^2 + y^2 <=1 then it is in the cirlce
        if(x**2 + y**2 <= 1):
            circleCount = circleCount + 1
      
    
    #once all of the points have been generated
    #find the ratio and return
    return (4*circleCount)/n

   




#try changing this number to see that as the number gets larger
#then we approach 3.141
print(simulatePi(10000000))
# at 10,000,000 the output was 3.142 which is pretty close t0
# the actual value of 3.1415

