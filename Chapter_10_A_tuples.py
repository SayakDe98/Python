#tuples are another kind of sequence that functions much like a list- they have elements which are indexed starting at 0
#tuples are reduced version of lists
#tuples are immutable whereas lists are mutable
x=("Glenn","Sally","Joseph")
print(x[2])
y=(1,9,2)
print(y)
print(max(y))

for iter in y:
    print(iter)

#y="ABC"
#y[2]="D"    #traceback:'str' object does not support item assignment this message is shown because strings are immutable


#z=(5,4,3)
#z[2]=0  #traceback:'tuple' object does not support item assignment

#things not to do with tuples:
#x=(3,2,1)
#x.sort()    #tuple doesn't have sort function

#x.append(5) #tuple doesn't have append function

#x.reverse() #tuple doesn't allow reversing

#a tale of two sequences:
#l=list()
#print(dir(l))   #in list we can use all these functions which getes listed by printing this function

#t=tuple()
#print(dir(t))

#tuples are limited lists.
#tuples are more efficient
# since python does not have to build tuple structres to be modifiable, they are simpler and more efficient in terms of memory 
#use and performance than lists

#so in our program when we are making "temporary variables" we prefer tuples over lists

#tuples and assignment
#we can also put a tuple on the left-hand side of an assignment statement
#we can even omit the paranthesis
(x,y)=(4,"fred")    #in tuple we can have variables on left side and their values on the right hand side
print(y)

(a,b)=(99,98)
print(a)

#the items() method in dictionaries returns a list of(key,value) tuples
d=dict()
d["csev"]=2
d["cwen"]=4
for (k,v) in d.items():
    print(k,v)

tups=d.items()
print(tups)

#tuples are comparable
#the comparision operators work with tuplesand other sequences.if the first item 
#is equal,python goes on to the next element, and so on, until it finds elements that differ.
print((0,1,2) <   (5,1,2))  
print((0,1,2000000)<(0,3,4))
print(("Jones","Sally")<("Jones","Sam"))#as l<m in Sally vs Sam hence our expression is True
print(("Jones","Sally")>("Adams","Sam"))#as J>A in Jones vs Adams hence our expression is True



