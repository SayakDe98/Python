#Inheritance

#When we make a new class - we can reuse an existing class and inherit all 
#the capabilities of an exisiting class and then add our own little bit to make our
#new class 

#another form of store and reuse

#write once-reuse many times

#the new class(child) has all the capabilities of the old class(parent)- and then some more

#Terminology:Inheritance

#'Subclasses' are more specialzied versions of a class, which inherit attributes and behaviours from 
#their parent classes, and can introduce their own

class PartyAnimal:
    x=0
    name=""

    def __init__(self,nam):
        self.name=nam
        print(self.name,"constructed")

    def party(self):
        self.x=self.x +1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):
    points=0
    def touchdown(self):
        self.points=self.points+7
        self.party()
        print(self.name,"points",self.points)

s=PartyAnimal("Sally")
s.party()

j=FootballFan("Jim")    #we use the constructor of PartyAnimal since we inherited FootballFan from PartyAnimal
j.party()
j.touchdown()

#FootballFan is a class which extends PartyAnimal. It has all the capabilites of PartyAnimal and more.

#Definitions:

#Class- a template
#Attribute-A variable within a class
#Method-A function within a class
#Object-A particular instance of a class
#Constructor-Code that runs when an object is created
#Inheritance-The ability to extend a class to make a new class

#Object Oriented programming is a very structered approach to code reuse.
#We can group data and functionailty together and create many independent instances of a class