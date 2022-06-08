#algorithms are a set of rules or steps used to solve a problem
#data structures are a particular way of organizing data in a computer
#a list is a data structure
#a list is a kind of collection
#a collection allows us to put many values in a single "variable"
#a collection is nice because we can carry all many values around in one convenient package.
#below two are collections:
friends=["Joseph","Glenn","Sally"]
carryon=["socks","shirt","perfume"]

#list constants are surrounded by square brackets and the elements in the list are sperated by commas
#a list element can be any python object - even another list
#a list can be empty
#below are some lists:
print([1,24,76])
print(["red","yellow","blue"])
print(["red",24,98,6])
print([1,[5,6],7])
print([])   #empty list

friends=["Joseph","Glenn","Sally"]
for friend in friends:
    print("Happy new year ",friend)
print("Done")

#looking inside lists
#just like strings, we can get at any single element in a list using an index specified in square brackets
friends=["Joseph","Glenn","Sally"]
print(friends[1])

#strings are immutable whereas lists are mutable
#immutable means we cannot change the contents of a string once created
#we can change contents of a list once created hence it is mutable

fruit="Banana"
#fruit[0]='b'    #there will be trackeback because strings are immutable
x=fruit.lower()
print(x)    #if we store a copy of a string in another variable then we can change the string
lotto=[2,14,26,41,63]
print("Before changing the value of list")
print(lotto)
lotto[2]=28
print("After changing the value of element at index 2 the list looks like:")
print(lotto)

#how long is a list?
#the len() function take a list as a paramter and returns the number of elements in the list
#actually len() tells us the number of elements of any set or sequence(such as string...)

greet="Hello Bob"
print(len(greet))   #len() here tells us the total no of characters in the string

x=[1,2,'joe',99]    #we can have combination of numbers strings etc
print(len(x))   #len() here tells us the total no of items in the list

#using the range function
#the range function returns a list of numbers that range from zero to one less than the paramter
#we can construct an index loop using for and an integer iterator
print(range(4))

friends=["Joseph","Glenn","Sally"]
print(len(friends))
print(range(len(friends)))

#we can use a for loop as below if we don't want the index:
for friend in friends:
    print("friend's name=",friend)

print("Alternate way:")
#we can use a for loop as below if we want the index as well:
for i in range(0,len(friends)):
    print("Index=",i," ,friend's name=",friends[i])

print("Alternate way:")
# we may not write the starting index too if we want:
for i in range(len(friends)):
    print("Index= ",i," ,friend's name=",friends[i])