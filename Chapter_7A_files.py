#a text file is a file which contains a sequence of lines
#to read a file we have to call the open() function first
# open() returns a "file handle"= a variable used to perform operations on the file
# Similar to "File->Open" in a Word Processor 
# handle=open(filename,mode) it returns a handle used to manipulate the file
# filename is a string
# mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file
# example: fhand=open('mbox.txt','r')
# UTF-8 is unicode character set
# the newline character
# we use a special character called the newline to indicate when a line ends
# we represent it a \n in strings
#newline is still one character-not two
stuff='Hellow\nWorld!'
stuff
print(stuff)
stuff='X\nY'    #\n is also a chracter but it is non printable
print(stuff)

print(len(stuff))