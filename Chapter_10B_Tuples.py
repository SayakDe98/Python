#Sorting List of Tuples...
#we can take advantage of the ability to sort a lit of tuples to get a sorted version of a dictionary
#first we sort the dictionary by the key using the items() method and sorted() function
#Sort by values instead of key
#if we could construct a list of tuples of the form(value,key) we could sort by value
#we do this with a for loop that creates a list of tuples
d={'a':10,'b':1,'c':22}
print(d.items())
print(sorted(d.items()))#key gets sorted

#using sorted()
#we can do this even more directly using the built-in function sorted that takes a sequence as a paramter and returns a sorted sequence
d={'a':10,'b':1,'c':22}
t=sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print(k,v)  #where k is key and v is value

#sort by values instead of key
#if we could construct a list of tuples of the form(value,key) we could sort by value

#we do this with a for loop that creates a list of tuples
c={'a':10,'b':1,'c':22}
tmp=list()  #creating a temporary data structre
for k,v in c.items():
    tmp.append((v,k))   #this is a tuple with first part as value and second part as key
print(tmp)  #ascending sort according to value

tmp=sorted(tmp,reverse=True)    #descending sort according to value
print(tmp)

#The top 10 most common words:
#fhand=open("romeo.txt")
#counts=dict()
#for line in fhand:
#    words=line.split()
#    for word in words:
#        counts[word]=counts.get(word,0)+1

#lst=list()
#for key,val in counts.items():
#    newtup=(val,key)
#    lst.append(newtup)

#lst=sorted(lst,reverse=True)

#for val,key in lst[:10]:
#    print(key,val)

c={'a':10,'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()])) 
