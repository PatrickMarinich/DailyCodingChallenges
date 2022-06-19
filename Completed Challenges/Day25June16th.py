#The Problem Hard

#Implement regular expression matching with the following special characters:
#. (period) which matches any single character
#* (asterisk) which matches zero or more of the preceding element
#That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
#For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
#Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.


#My Notes:
#attempt 1
#My plan will be to check each character in the string and match them up one to one. if there is a descrepency then return false, if not then return true.
#the asterisk is the tricky part of this challenge. So my plan will be to append the characters that I have already checked to an empty list so that I can 
#look back and see if there was a character used before



#if the phrase matches the key, to all of the characters then return true. if not then return false.
#follow the special rules for . and *
def expressionMatch(phrase,key):

    #store the values checked for the *
    checked = []

    #if the lengths arnt the same then just return false
    if len(phrase) != len(key):
        return False


    for i in range(len(phrase)):
        #check to see if the character is a . or *
        if phrase[i] == '.':
            checked.append(phrase[i])
        elif phrase[i] == '*':
            #check if checked has a period id it does then were good, if not then it has to check the letter
            if '.' not in checked:
                #if its not here then return false
                if key[i] not in checked:
                    return False
            #if it makes it here then it is a pass
            checked.append(phrase[i])
        else:
            #this would be a normal character check
            if phrase[i] != key[i]:
                return False
            checked.append(phrase[i])

    #if it makes it here then it is good!
    return True
                

#tests!

print(expressionMatch('ra.','ray'))   #true
print(expressionMatch('ra.','raymond'))  #false
print(expressionMatch('.*at','chat'))  #true
print(expressionMatch('.*at','chats')) #false
print(expressionMatch('.*at','bruh'))  #false

print(expressionMatch(".atr.c.", "patrick")) #true

print(expressionMatch('ap*l.s','apples')) #true
