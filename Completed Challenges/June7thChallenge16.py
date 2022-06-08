#The Problem (Easy)
#You run an e-commerce website and want to record the last N order ids in a log. 
#Implement a data structure to accomplish this, with the following API:

#record(order_id): adds the order_id to the log
#get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
#You should be as efficient with time and space as possible.


#notes
#create a class with a field of an array. record(id) appends to that array
#and get_last(i) will return the value at len(log) - i since it is backwards

# My solution


class OrderLog:
    #can store the order logs of an ecommerse website
    log = []
    #the only paramater is the size which is n
    def __init__(self,n):
        self.max_size = n

    #if the log is longer then max_size, pop and add, if else
    #just add
    def record(self,order_id):
        if (len(self.log) > (self.max_size)):
            self.log.pop(0)
            self.log.append(order_id)
        else:
            self.log.append(order_id)

    
    #returns the value of the ith item in the log, if 
    #i is longer then the log, then just return none
    #if i is not, then return the value at the ith position
    def get_last(self,i):
        if ( i > len(self.log)):
            return None
        else: return self.log[i]

        

#tests
  
log = OrderLog(10)

#tests to see what will happen when the log over flows,
#expected result is that the olest values will go away and the array will
#slide down
for i in range(15):
    log.record(i)
    print(log.log)
    
print(log.get_last(5)) #9 is expected

        


        

