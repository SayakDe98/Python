#Dictionaries;Common Applications

#many counters with a dictonary
#one common use of dictionaries is counting how often we "see" something
ccc=dict()
ccc["csev"]=1
ccc["cwen"]=1
print(ccc)
ccc["cwen"]=ccc["cwen"]+1
print(ccc)

#dictionary traceback
#it i an error to reference a key which is not in the dictionary
#we can use the in operator to see if a key is in the dictionary
ccc=dict()  #this is a fresh dictionary
#print(ccc["csev"])#since it is a fresh dictionary hence there won't be anything
print("csev" in ccc)#using in operator

#when we see a new name 
#when we encounter a new name , we need to add a new entry in the dictionary and if this the second or later time we have seen the name,
#we simply add one to the count in the dictionary under that name
counts=dict()
names=["csev","cwen","csev","zqian","cwen"]
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)

#the get method for dictionaries
#the pattern of checking to see if a key is already in a dictionary and assuming a defauly value if the key is not there is so common that there is a method called get() that does this for us
#default value if key does not exist(and no Traceback)
if name in counts:
    x=counts[name]
else:
    x=0
x=counts.get(name,0)
print(x)

#simplified counting with get()
#we can use get() and provide a default value of zero when the key is not yet in the 
#dictionary - and then just add one
counts=dict()
names=["csev","cwen","csev","zqian","cwen"]
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)