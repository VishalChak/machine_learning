

day = "Sunday"
abbreviation = day[:3]
print abbreviation




numbers = range(0,40)
evens = numbers[2::2]
evens



#Booleans and Truth Testing

if day == "Sunday":
    print "Sleep in"
else:
    print "Go to work"


day == "Sunday"



1 == 2



50 == 2*25



1 ==1.0


1 is 1.0



#boolean tests on lists
[1,2,3] == [1,2,4]



[1,2,3] < [1,2,4]



#Multiple comparisons
hours = 5
0 < hours < 24




if day == "Sunday":
    print "Sleep in"
elif day == "Saturday":
    print "Do chores"
else:
    print "Go to work"



#Adding for 
days_of_the_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for day in days_of_the_week:
    statement = "Today is " + day
    print statement
    if day == "Sunday":
        print "   Sleep in"
    elif day == "Saturday":
        print "   Do chores"
    else:
        print "   Go to work"



bool(1)




bool(0)



bool(["This "," is "," a "," list"])



#The Fibonacci Sequence
n = 10
sequence = [0,1]
for i in range(2,n): # This is going to be a problem if we ever set n <= 2!
    sequence.append(sequence[i-1]+sequence[i-2])
print sequence



#Quiz :WAP to generate seq of sqrs



#Functions
def fibonacci(sequence_length):
    "Return the Fibonacci sequence of length *sequence_length*"
    sequence = [0,1]
    if sequence_length < 1:
        print "Fibonacci sequence only defined for length 1 or greater"
        return
    if 0 < sequence_length < 3:
        return sequence[:sequence_length]
    for i in range(2,sequence_length): 
        sequence.append(sequence[i-1]+sequence[i-2])
    return sequence




fibonacci(2)




fibonacci(12)




help(fibonacci)


# In[23]:

#Recursion and Factorials
from math import factorial
help(factorial)




factorial(20)


# In[25]:

def fact(n):
    if n <= 0:
        return 1
    return n*fact(n-1)



fact(20)




#Two More Data Structures: Tuples and Dictionaries Tuples are like lists but immutable
t = (1,2,'hi',9.0)
t




t.append(7)



t[1]=77



('Bob',0.0,21.0)



#List
positions = [
             ('Bob',0.0,21.0),
             ('Cat',2.5,13.1),
             ('Dog',33.0,1.2)
             ]


# In[78]:

#Tuple assignment to swap variables
x,y = 1,2
y,x = x,y
x,y



#Dictionaries are an object called "mappings" or "associative arrays" in other languages. Whereas a list associates an integer index with a set of objects:
#The index in a dictionary is called the key, and the corresponding dictionary entry is the value. A dictionary can use (almost) anything as the key. Whereas lists are formed with square brackets [], dictionaries use curly brackets {}:




ages = {"Rick": 46, "Bob": 86, "Fred": 21}
print "Rick's age is ",ages["Rick"]




dict(Rick=46,Bob=86,Fred=20)



len(t)




len(ages)


#break statement
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
         # loop fell through without finding a factor
        print n, 'is a prime number'



#Continue statement
for num in range(2, 10):
     if num % 2 == 0:
        print "Found an even number", num
        continue
        print "Found a number", num





