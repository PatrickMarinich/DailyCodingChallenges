#the problem

#Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
# return all strings in the set that have s as a prefix.

#For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

#Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


#notes
#use the python find command to see if there is a sub string, if it does not equal -1 then it exists so then
#append to an answer arrya

#my solution
def autoCorrect(query, possible):

    #check every string in the set of possibilities

    #answers will fill with any values that it could be
    answers = []
    for currString in possible:
        if(currString.find(query) != -1):
            answers.append(currString)

    return answers

#tests
input = 'de'
possible = ['dog', 'deer', 'deal']

input1 = 'hi'
possible1 = ['hight','hype','hi','high','apc']

print(autoCorrect(input,possible)) #expected [deer, deal]
print(autoCorrect(input1,possible1)) # expected everthing but hype and apc
print(autoCorrect(input,possible1)) #expected []

