fruit='banana'#this is a comment in python

letter=fruit[1]

print(letter)

x=3

letter=fruit[x-1]

print(letter)

print(len(fruit))#prints the length of string

#for loop
fruit="Banana"
count=0
for i in fruit:
    print(count,i)
    count=count+1

#while loop
index=0
while index <   len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1


for letter in fruit:
    print(letter)
    
#loop to check number of a's in a loop
count=0
word="Banana"

for letter in word:
    if letter=='a':
        count=count+1

print("Number of a's in word is :",count)

