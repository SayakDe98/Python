#slicing strings
#<variable name>[starting_index:ending_index+1]
s="Sayak"
print(s[0:3])   #prints Say
print(s[3:4])   #prints only character at index 3

s1="I am doing my best out here"
print(s1[6:10])

#we can eliminate the first index,we can eliinate the ending index,we can eliminate both

#we eliminate the first index:
print(s1[:10]) #prints from position 0(starting index) to 9

#we eliminate the last index:
print(s1[6:])   #prints from 6 to last index

#we can eliminate both first and last index then we get the full string
print(s1[:])

#we can concatenate strings in python using + operator
a="Hi"
c=a+" there"
print(c)

b="friend"
c=a+b
print(c)

#using in as a logical operator,previously we used it as an iterator
#the in keyword can also be used to check to see if one string is "in" another string
#the in expression is a logical expression is a logical expresion that returns True or False and can be used in an if statement

fruit='banana'

print('n' in fruit)    #outputs True because n is present in fruit

print('m' in fruit)    #outputs False because m is absent in fruit

print('nan' in fruit)  #outputs True because nan is present in fruit

if 'a' in fruit:
    print('Found it!')

#string comparision
word='banana'
if word=="banana":
    print("All right,bananas.")

if word     <   "banana":
    print("Your word, "+word+", comes before banana.")
elif word   >   "banana":
    print("Your word,"+word+",comes after banana")
else:
    print("All right, bananas.")   
    
#ord() is used to get the ascii value of a character
print("Using ord()")
myWord="banan"
sum=0
for letter in myWord:
    sum=sum+ord(letter)
sum1=0
for letter in "banana":
    sum1=sum1+ord(letter)

if myWord=="banana":
    print("All right bananas")
elif sum<sum1:
    print("your word comes before banana")
else:
    print("your word comes after banana")

#strings are objectsin python and java.strings have built in methods
#we have string library in python where inbuilt functions of strings are present
#these functions are already built into every string we invoke them by appending the function to the string variable
#these functions do not modify the original string,instead they return a new string that has been altered
greet="Hello bob"
zap=greet.lower()   #python equivalent of java's .toLower()
print(greet)
print(zap)
print("Hi There".lower())   # Hi There is a string constant, Hi There is not an object

stuff="Hello World"
print(type(stuff))  #prints the data type

print(dir(stuff))   #prints all the methods that are available for stuff i.e. string class

print(stuff.upper())    #python equivalent of java's .toUpper()

fruit="banana"
pos=fruit.find("na")    #used to find the starting index of "na" in "banana" 
print(pos)

aa=fruit.find("z")   #used to find the starting index of "z" in "banana" 
print(aa)   #prints value of -1 since z is absent in the string fruit

#search and replace
#the replace() function is like a "search and replace" operation in a word processor
#it replaces all occurences of the search string with the replacement string

greet="Hello Bob"
print("Before replacing : ",greet)
print("After replacing : ",greet.replace("Bob","Sayak"))

print("After replacing o with x : ",greet.replace("o","x"))

#stripping whitespace
#whitespace is space tab newline or any character that prints nothing
#sometimes we want to take a string and remove whitespace at the beginning and/pr end
#lstrip() and rstrip() is used to remove whitespace at the left or right
# strip() removes both beginning and ending whitespace

greet="    Hello bob   "
print("Left strip:",greet.lstrip())
print("Right strip:",greet.rstrip())
print("Stripping both sides:",greet.strip())

#prefixes areused to find out if an object is string with something
line="Please have a nice day"
print("line starts with 'Please' : ",line.startswith("Please"))
print("line starts with 'p' : ",line.startswith('p'))

#parsing and extracting 
#let's extract the uct.ac.za from the data below
data="From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008"
atpos=data.find('@')    #starting position
print(atpos)
sppos=data.find(" ",atpos)  #ending position
print(sppos)
host=data[atpos+1 : sppos]
print(host)

#in python 3 all strings are in unicode unlike python 2
#check the video scientific computing with python freecodecamp for detailed understanding
#  
