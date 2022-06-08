#python has object oriented approach to its operators
# + can add integer,floating point numbers ,etc
# similarly we can add lists using + operator
#we can create a new list by adding two existing lists together
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
print(a)

print("Next set of codes:")
#lists can also be sliced like strings
t=[9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

#there are a number of different methods for list we can get to know which are the methods by using dir function
x=list()
print(type(x))  #prints out the data type of variable x
print(dir(x))   #prints out all the methods of lists

#building a list from scratch:
#we can create an empty list and then add elements using the append method
#the list stays in order and new elements are added at the end of the list
stuff=list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

#is something in a list?
#python provides two operators that let you check if an item is in a list
#these are logical operators that return True or False
#they do not modify the list
some=[1,9,21,10,16]
print(9 in some)    #9 is present in the list
print(15 in some)   #15 is absent in the list
print(20 not in some)   #20 is absent in the list

#lists are in order
#list can hold many items and keeps those items in the order until we do something to change the order
#a list can be sorted(i.e. change its order)
#the sort method(unlike in strings) means "sort yourself"
friends=["Joseph","Glenn","Sally"]
friends.sort()  #sorting in ascending order . sorting possible in lists not possible in strings
print(friends)
print(friends[1])

#there are a number of functions built into python that take lists as paramters
#by using the lists below we don't need to write loops for doing the functions below:
nums=[3,41,12,9,74,15]
print("Length of list: ",len(nums))
print("Maximum value in list: ",max(nums))
print("Minimum value in list: ",min(nums))
print("Sum of all values in list: ",sum(nums))
print("Average of all values in list: ",sum(nums)/len(nums))

#let's see two approaches:
#first approach this uses lesser memory among the two:
print("First Approach:")
total=0
count=0
while True:
    inp=input("Enter a number: ")
    if inp=="done":break
    value=float(inp)
    total=total+value
    count=count+1
average=total/count
print("Average=",average)

#this second approach uses more memory
print("Second approach:")
numlist=list()
while True:
    inp=input("Enter a number: ")
    if inp=="done":break
    value=float(inp)
    numlist.append(value)
print("Average=",sum(numlist)/len(numlist))