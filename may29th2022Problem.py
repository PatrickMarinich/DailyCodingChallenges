#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#You can assume that the messages are decodable. For example, '001' is not allowed.


#given a string, give the count of possible decodings


from math import factorial

def decodeCount(strIn):

    total_count = 1

    strIn = str(strIn)
    #put all of the numbers into an array
    numbers = []
    for i in range(len(strIn)):
        numbers.append(strIn[i])

    #go through array:
    consec = 1
    counts = []
    currGroups = 0
    for i in range(len(numbers)):
        if(i != len(numbers)-1):
            if(int(numbers[i])*10 + int(numbers[1+i]) <= 26):
            #if the numbers are less than 26
                currGroups += 1
            else:
                #group is broken
                if(currGroups > 1):
                    #notes are below for why this formula is correct
                    counts.append((factorial(currGroups) / (2*factorial(currGroups -2)) + 2))
                    currGroups = 0
                elif currGroups ==1:
                    counts.append(2)
                    currGroups = 0
        else:
             #group is broken
                if(currGroups > 1):
                    #notes below for this math
                    counts.append((factorial(currGroups) / (2*factorial(currGroups -2)) + 2))
                elif currGroups == 1 :
                    counts.append(2)
                    currGroups = 0
                
    
    #at the end multiply all of the values in count
    for values in counts:
        total_count *= (values)
    #return this value
    return total_count


            



#tests
print(decodeCount(11111))  # expected 8
print(decodeCount(111)) #expected 3
print(decodeCount(9999)) #expected 1
print(decodeCount(1221)) #expected 5
print(decodeCount(12921)) #expected 4
print(decodeCount(1234567)) #expected 3




#NOTES

    #figure out how the numbers can be read

    #example 1234567 - 3, groups 
    #possibilies
    #abcdefg
    #lcdefg
    #awdefg
    
    #example 1221 - 5   groups choose 2 + 2 
    #abba
    #lba
    #abv
    #lv
    #axa

    #example
    #11111 - 8  groups choose 2 + 2
    #aaaaa
    #kaaa
    #akaa
    #aaka
    #aaak
    #akk
    #kak
    #kka

    #math:
    #for consecutive numbers that can all be changed
    # ie 122121, the combonation is (groups choose 2) + 2
    #for numbers not consecutive ie
    #9229, then there are 2 ways it can be read
    #if there is a combination of these then multiply,
    #1221219229 would be 
    # (5 choose 2 + 2) * 2


   


    

    
    




