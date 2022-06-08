#counting words in text
#counting pattern:
#the general pattern to count the wordsina line of text is to split the line
#the line into words, then loop through the words and use a dictionary to track the
#count of each word independently
counts=dict()
print("Enter a line of text:")
line=input("")

words=line.split()

print("Words:",words)

print("Counting...")
for word in words:
    counts[word]=counts.get(word,0)+1
print("Counts",counts)

#Definite loops and dictionaries
#even though dictionaries are not stored in order, we can write a for loop that goes
#through all the entries in a dictionary-actually it gos through all of the keys
#in the dictionary and looks up the values
count={"chuck":1,"fred":42,"jan":100}
for key in count:
    print(key,count[key])

#Retrieving lists of keys and values
#you can get a list of keys,values or items(both) from a dictionary
jjj={"chuck":1,"fred":42,"jan":100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#Bonus:Two Iteration Variables!
#we loop through the key-value pairs in a dictionary using *two*
#iteration variables
#each iteration , the first variable is the key and the second variable is the 
#corresponding value for the key
jjj={"chuck":1,"fred":42,"jan":100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)

name=input("Enter file:")
handle=open(name)

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1   #this is a histogram.
        #a histogram is basically used to represent data provided in a form of some 
        #groups.It is accurate method for the graphical representation of numerical data distribution.
#count[words]=counts.get(word,0)+1 is a histogram 

#we are using two variables in the loop
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)