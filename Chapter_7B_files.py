#we can strip the whitespace from the right-hand side of the string using rstrip() from the string library
# the newline is considered "white space" and is stripped
#File Handle as a sequence
#A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
# we can use the for statement to iterate through a sequence
# remember - a sequence is an ordered set

xfile=open('mbox.txt')  #xfile is file handler used to open files
for cheese in xfile:#using for loop to access content of mbox.txt
    print(cheese)  #prints all the content inside xfile

#counting lines in a file
#open a file read-only
#use a for loop to read each line
#count the lines and print out the number of lines
fhand=open('mbox.txt')
count=0
for line in fhand:
    count=count+1
print("Line count : ",count)

#we can read the whole file(newlines and all) into a single string can be done using read() function
fhand=open("mbox.txt")
inp=fhand.read()
print(inp)
print(len(inp))
print("The first 20 characters:",inp[:20])

#searching through a file
#we can put an if statement in our for loop to only print lines that meet some criteria
fhand=open("mbox.txt")
for line in fhand:
    if line.startswith("this"):
        print(line)

#in the above text file why is there another new line?it's because we have pressed enter after every line
#and the print statement adds another new line,hence we get another new line

#How to fix the above error? we use rstrip which strips all the whitespace from the right hand side of the string 
print("After fixing the error:")
fhand=open("mbox.txt")
for line in fhand:
    line=line.rstrip()
    if line.startswith("this"):
        print(line)

#alternate way:
print("alternate way:")
fhand=open("mbox.txt")
for line in fhand:
    line=line.rstrip()
    if not line.startswith("this"): #this is not the line we want to print
        continue
    print(line)

#another alternate way:
print("Another alternate way:")
fhand=open("mbox.txt")
for line in fhand:
    line=line.rstrip()
    if not "this" in line:  #using the in operator
        continue
    print(line)

#let's get the filename from user
print("Enter file name:")
s=input()
fhand=open(s)
count=0

for line in fhand:
    line=line.rstrip()
    if line.startswith("this"):
        count=count+1
print("Number of lines:",count)

#now let's see how to handle bad file names
fname=input("Enter the file name:")
try:
    fhand=open(fname)
except:
    print("File cannot be opened",fname)
    quit()

count=0
for line in fhand:
    line=line.rstrip()
    if line.startswith("this"):
        print(line)
        count=count+1
print("Number of lines in the file is:",count)
