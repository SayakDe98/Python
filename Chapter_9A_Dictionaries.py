#what is a collection?
#a collection is nice because we can put more than one value in it and carry them all around in one convienient package
#we have a bunch of values in a single "variable"
#we do this by having more than one place "in" the variable
#we have ways of finding the different places in the variable

#what is not a collection?
#most of our variables have one value in them-when we put a new value in the variable-the old value is overwritten

#a story of two collections
#list:
#a linear collection of values that stay in order

#a dictionary:
#a "bag" of values, each with its own label(key),they aren't stored in order

#dictionaries are python's most powerful data collection
#dictionaries allow us to do fast database-like operations in python
#dictionaries have different names in different languages
#associative arrays-perl/php
#properties or map or hashmap-java
#property bag-C#/.Net
#lists index their enteries basedon the position in the list
#dictionaries are like bags-no order
#so we index the things we put in the dictionary with a "lookup tag"
purse=dict()
purse["money"]=12
purse["candy"]=3
purse["tissues"]=75
print(purse)

print(purse["candy"])
purse["candy"]=purse["candy"]+2
print(purse)

#comparing lists and dictionaries
#dictionaries are like lists except that they use keys instead of numbers to look up values
lst=list()
lst.append(21)
lst.append(183)
print(lst)
lst[0]=23
print(lst)
ddd=dict()
ddd["age"]=21
ddd["course"]=182
print(ddd)
ddd["age"]=23
print(ddd)

#dictonary literals(constants)
#dictionary literals use curly braces and have a list of key:value pairs
#you can make an empty dictionary using empty curl braces
jjj={"chuck":1,"fred":42,"jan":100}
print(jjj)
ooo={ }
print(ooo)