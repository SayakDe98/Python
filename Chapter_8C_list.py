#split breaks a string into parts and produces a list of strings. we think of these as words.we can access 
#a particular word or loop thorugh all the words.
abc="With three words"
stuff=abc.split()
print(stuff)

print(len(stuff))
print(stuff[0])
print(stuff)
for w in stuff:
    print(w)

#when you do not specify a delimeter, multiple spaces are treated like one delimeter
#you can specify what delimeter character to use in the splitting
line="A lot                         of spaces"  #a bunch of whitespace is treated as one space
etc=line.split()
print(etc)

line="first;second;third"
thing=line.split()
print(thing)
print(len(thing))
thing=line.split(";")
print(thing)
print(len(thing))

fhand=open("mbox1.txt")
for line in fhand:
    line=line.rstrip()
    if not line.startswith("From"):continue
    words=line.split()
    print(words[2])

#sometimes we split a line one way , and then grab one of the pieces of the line and split that piece again
words=line.split()  #splitting once
email=words[1]
pieces=email.split("@") #splitting second time
print(pieces[1])
