#Extracting a host name-using find and string slicing
data="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos=data.find("@")
print(atpos)#prints out the index of @ in data

sppos=data.find(" ",atpos)
print(sppos)#prints the first whitespace after index atpos 

host=data[atpos+1   :   sppos]
print(host) #prints out chracters from index atpos+1 to sppos-1

#The Double Split Pattern
#Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again

line="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
words=line.split()  #splits line into different words
email=words[1]  #takes the 2nd word in email
pieces=email.split("@") #splits the email and stores into two parts stephen.marquard and uct.ac.za
print(pieces[1])    #prints the second part of email that is : uct.ac.za

#The Regex Version
import re
lin="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y=re.findall("@([^ ]*)",lin)    #look through the string until you find an at sign,[^ ]is used to match non-blank character,* match many of them
print(y)

# ^ means Starting at the beginning of the line, look for the string "From"
y=re.findall("^From .*@([^ ]*)",lin)    #^ means starting at the beginning of the line, From means look for the string "From"
print(y)

#Spam Confidence
import re
hand=open("mbox2.txt")#Create a file for which regex will be written
numlist=list()
for line in hand:
    line=line.rstrip()
    stuff=re.findall("^X-DSPAM-Confidence:  ([0-9.]+)",line)    #[0-9.] means digits or dots
    if len(stuff)!=1 :continue
    num=float(stuff[0])
    numlist.append(num)
print("Maximum:",max(numlist))

#Escape Character
#If you want a special regular expression chracter to just behave normally(most of the time) you prefix it with '\'
import re
x="We just recieved $10.00 for cookies."
y=re.findall("\$[0-9.]+",x) #$ means a real dollar sign,0-9 are the range of numbers . is period,+ is atleast one or more
print(y)

#Regular expressions are a cryptic but powerful langauge for matching strings and extracting elements from those strings
# Regular expressions have special characters that indicate intent 