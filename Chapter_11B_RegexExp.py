#matching and extracting:
#re.search() returns a True/False depending on whether the string matches the regular expression
#if we actually want the matching strings to be extracted, we use re.findall()
#[0-9]+ we are enclosing numbers inside square brackets only when we need multiple numbers
import re   #re library is regular expression
x="My 2 favourite numbers are 19 and 42"
y=re.findall("[0-9]+",x)    #findall() gives a list of all those strings that match.0-9 is a single digit. when we write a + after the square brackets it means one or more digits
print(y)    #gives out one or more digits it pulls them and out and gives it back to me
#parsed it,split it and found all these things
y=re.findall("[AEIOU]+",x)
print(y)
#Warning:Greedy Matching
#The repeat characters (* and +) push outward in both directions(greedy) to match the largest 
#possible string
import re
x="From: Using the : character"
y=re.findall("^F.+",x)
print(y)
# ^F.+: where F is the first character in the match is an F,+ is one or ore charcters,: is last character in the match is a ":"
#the greedy algo says if it can match with more number of words then it will do that

#Non-Greedy Matching
#Not all regular expression repeat codes are greedy!
#If you add a ? character, the + and * chill out a bit...
import re
x="From: Using the : character"
y=re.findall("^F.+?:",x)    #if we use .+? means one or more characters but non greedy.so we pick only one word
print(y)

#Fine-Tuning String Extraction
#You can refine the match for re.findall() and seperately determine which portion of the match is to be extracted by using paranthesis
x="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y=re.findall('\S+@\S+',x)   # \S means atleast one whitespace
print(y)

#Fine-Tuning String Extraction
#Paranthesis are not part of the match-but they tell where to start and stop what string to extract

y=re.findall("\S+@\S+",x)
print(y)
y=re.findall("^From (\S+@\S+)",x)   #this means exclude "From" and take only whats inside the paranthesis
print(y)