#problem
#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

#notes 
# the easy way to do this would be to just create a function that uses sleep and calls the function in the paramater
#since this is python, the function can just be directally passed into the function, however if this was C or another language
# then something in the exec family would have to be used with a function pointer


#my first solution
from os import fork
import time
def Schedule(f,n):
    #divide by 1000 for milliseconds
    time.sleep(n/1000)
    f()


#however there would be a better solution, this would be to fork the porvess so that the origional process could still
#do whatever it is supposed to do while having the child wait to run the process
#however this does not work on windows as windows does not support forking apperently
def improvedSchedule(f,n):

    pid = fork()

    if pid == 0:
        time.sleep(n/1000)
        f()
    else:
        print("continue doing any other application that the scheduler would be doing")


#tests
def test():
    print("hi this is generated from the 'test' function")

Schedule(test,1000)
#improvedSchedule(test,2000)

