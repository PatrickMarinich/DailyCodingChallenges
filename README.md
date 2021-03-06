# DailyCodingChallenges
A Place where I upload my solutions to a daily coding challenge that I create from a challenge problem I am given from a mailing list.

**Note:** The challenge solutions in the completed challenges folder are 100% my own, however, the problems themselves are not my own, they are from DailyCodingChallenge.com

**Contents**
* Completed Challenges 
    * All of my solutions to the different daily challenges
    * These Files all Include:
        * The Probelm
        * My Solution
        * Tests
        * Good Documentation on my thoughts and code (Hopefully!)
* Non-Completed Challenges
    * Any challenge that I have read from the email or started but have not finished yet.
    * These may be a files with an untested, partial, incomplete, or incorrect solution that I came up with
    * These may be a files with code snippits or possible ideas
    * These may even be just the problem commented with no code so I can start it later
* Setup
    * Any files nessassary for the set up of vscode or complieiers for different languages

**My goals with these challeges:**
1. Continue to develop my software skills throughout the year.
2. Learn new features within what language I am solving a problem in.
3. Solve difficult problems involving data structures and analysis to sharpen my skills and problem solving abilities
4. Take the time to improve my documentation, so that if somebody is looking at one of my solutions they would be able to understand what my code does
5. Solve some intresting and tricky problems.

The challenges come from the mailing list of DailyCodingProblem.com, I will include the possible solution that I came up with each day that I complete the challenge. These challenges leave alot of room up to the developer to create their own unique solution, thus my solutions may look completely different then if another person decided to do the specific challenge. 

**Personal Rules:**
1. All solutions are my own, no code is from anybody else
2. If a topic or question is outside of my knowledge, then I may use the internet to research the topic without looking up a specific code solution
3. If I miss a day or cannot solve a problem in the moment, I can resume later and go back to it (these are not timed problems)
4. This is a learning experiance as much as it is a challenge, so I will be trying to accomplish all of the bonus or follow-ups aswell to the best of my ability
5. Document my thinking porcess as if somebody who has never coded is trying to understand what is accomplised

**My Background in Software before starting these challenges:**
1. College Class in Java
2. College Class in Object Oriented Programming
3. College Class in C and Systems Programming
4. College Class in Data Structures
5. Self Taught in Python, inclduing projects using Keras and Pandas 
6. MATLAB usuage in my Engineering Classes
7. Lab courses where I was able to use Excel, Python, and Verilog at my dicression

**The format of each of the code files starting May 31st 2022 will be:**
1. The problem (copy and pasted from the email)
2. Any notes that I may have, either from my thought process, my research, or examples (in the future, I will even include my throughts for incorrect attempts to show where I started and how I arrived at the solution)
3. The Code Solution I developed
4. Tests of some kind to show that my solution works. 

In each of the code files I do some documentation on my thought process behind what my code does, however it may not be the most detailed explination of what is exactly going on, I am hoping to improve my documentation skills overtime by completing these challenges. Below are some notes on the challenges as well they are numbered in order of completion.

Below is a table of entires for each of the challenges that I've completed, they are in the format of:
* Completed #, Date assigned, Difficulty Level, My Difficulty Score, Breif Topic Description

**Completed Days:**
1. May 23rd 2022, Easy, 2/10, Checking for summed values in an Array
2. May 24th 2022, Hard, 3/10, Multiplication of specific array elements
3. May 26th 2022, Hard, 6/10, Looking for consecutive positive integers in an unsorted array
4. May 25th 2022, Medium, 9/10, Binary Tree serialization and deserialization
5. May 30th 2022, Easy, 8/10, Unival Subtrees in a Binary Tree
6. May 29th 2022, Medium, 7/10, Combinations with decoding
7. May 31st 2022, Hard, 9.5/10, Largest non-adjecet sum in an array
8. June 1st 2022, Medium, 3/10, Creating a schedule that calls a function after a delay
9. June 2nd 2022, Medium, 1/10, Auto-Fill Implementation
10. June 5th 2022, Medium, 3/10, Monte Carlo Approx of Pi
11. June 7th 2022, Easy, 2/10, Creating a DataLog Class
12. June 12th 2022, Easy, 1.5/10, Finding Minimum Classes needed given time intervals
13. June 13th 2022 Easy, 3/10, Finding an intersencting node in 2 linked lists
14. June 16th 2022, Hard, 6/10, Auto Complete using special characters
15. June 17th 2022, Medium, 4/10, Linked List backwards removal

**Any Notes About My Solution**
1. A bit tricky to find optimization to complete the bonus aspect
2. My first solution answered the follow up, I am upset with myself that I did not even consider the easier approach by just using division, I think that the tag of HARD from the email led me to think of more complex solutions without even considering easy ones
3. My idea for the solution came quickly, however broke when repeating numbers were added into the array, finding this solution took me a couple extra minutes, and accounted for the majority of my dev time for this challenge
4. The most challenging thus far. This may have came from my misintrepretation of using a binary search tree rather than 
    a binary tree as specified in the problem. I was a bit rusty when creating my insert function. Overall Tough but fun! I had to use a ton of recursion which is great practice.
5. Another challenging one, marked as easy in the email, however I found this to be more difficult. My knowlage on trees and their implimantation must be   the main cause of the struggles that I face here. Overall My solution worked as I expected it too however it took me a bit to get it fully implemented correctally. This challenge gave me a bunch of pracice with python recursion and binary trees, and introduced me to the concept of unival trees. My solution included 3 helper methods, one to do a check if a subtree was unival, one to count the nodes of the sub tree, and one to iterate through each node in the orgional tree
6. The difficulty of this challange came from the theory aspect rather then the implementation. Once I figured out the combinitoric formula, then it was a pretty easy implementation. I would give the implementation a 3 or 4 out of 10, however the difficulty of the combinitorics problem defnietly bumps up the challenge of this problem. Next time when presented with a problem like this, I should break out a pen and paper rather then trying to do mental gymnastics, I probably would have saved 15 or so munites. Overall a great combinitorics challenge!
7. Increadibly difficult challenge. There were so many edge cases to account for which made finding a possible solution algorythem very difficult. My solution is probably not the most efficient way to accomplish this, however it is the one that I thought of after some trial and error. This definietly took some time and thinking to solve. My solution was able to keep the complexity in O(n) but I think that there may be a more efficient algorythem to be discovered in the future. I would like to come back to this problem in a year or two to see if my approach would have changed or if I would have new insight into a new possible solution. Overall I am happy that my solution did end up working as I thought albeit after some trial and error with different approaches.
8. Before doing this challenge I have had experiance with exec and forking in C, and thus was easily able to transfer this to python. However I was unaware that the windows os does not directally support forking, thus I spent a decent amount of time trying to figure out why my fork solution did not work on my machine. However it would work on Mac or Linux as it a only a few lines of code and thus most likely does not have any bugs. The easy solution was just to use the python time.sleep and then invoking the function paramater. If this was written in C then I would have had to use a function pointer and an exec command. Overall not a difficult solution to think of at all given the past experiances ive had with this topic
9. The solution to this problem came within 30 seconds or so. The implementation is just looking for substrings within a set of strings. depending on the language this implementation would be slightly different, but since I was in python the only command I have to use was find(). if I was solving this problem in C for example i would have had to use the strstr() function. Overall not very difficult, I did disregard the hint however as I could not think of a data structure that would be faster then a list. Also using a for each loop is the most convient way to implement this solution (in python anyways)
10. The pure math implementation challenges are very fun to undertake. It was very satisifying to find my approximation of pi using the area of a circle and a square. It was also pretty cool to run this simulation and really see the number approach 3.141. Overall not a very difficult challenge, but a fun one.
11. The first challenge that involved making a class other then a node. It was pretty simple to implement as it was just an array, however it was nice to use OOP programming within this challenge as it has been a little while since I have done work with OOP. Overall I liked the idea of the datalog, and anthough it was pretty easy to implement it was still a nice challenge to complete.
12. Overall not a difficult solution, it came pretty fast, the challenge would be to optimize this solution. Overall I enjoy these more practical challenges where the problem is something that can directally be seen in real life rather then an abstract concept that has application but that applicaiton is not directally represented in the problem.
13. Since the nodes were considered to be the same if the value was the same, then it was a pretty easy task as I was able to just store the values of the first linked list in an array, and then use those saved values to check the second list rather then interating through the entire linked list multiple times
overall an interesting though challenge however not too difficult. Due to work and other things I have fallen behind on completing some of these challenges, the brightside is now I have a pool to challenges that I can tackle when I find some of them interesting and have the spare time to do them! Cannot wait to complete more of these challenges in the future.
14. This was an interesting thought experiment, I liked the challenge of trying to figure out an easy way to implement something such as an auto correct or wildcard character. Overall once I had the idea for the * character the rest of the puzzle filled in iteself, overall the code was not anything too overly complex, the challenge was more difficult due to the idea of wildcards themselves.
15. This challenge was a simple ask however turned out to be a bit more challenging then expected. My first thought eneded up being a correct solution to this problem, but I sat on this problem for a couple of days trying to find an efficient way to only do it with one pass through. I settled on recursive calls of a function. This may not be the most efficient implementation, but it definietly passed the requirements of the challenge.
