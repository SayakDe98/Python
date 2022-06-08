#Object LifeCycle:

#Objects are created, used and discarded

#We have special blocks of code(methods) that get called
    #At the moment of creation(constructor)
    #At the moment of destruction(destructor)

#Constructors are used a lot

#Destructors are seldom used

#Construtor 
#The primary purpose of the constructor is to set up some instance variables to
#have the proper initial values when the object is created

class PartyAnimal:
    x=0 #data member

    def __init__(self): #this is a constructor
        print("I am constructed")

    def party(self):    #this is a method/member function
        self.x=self.x+1
        print('So far',self.x)

    def __del__(self):  #this is a destructor
        print("I am destructed",self.x)

an=PartyAnimal()
an.party()
an.party()

an=42   #as we do this it destroys object an, this is where destructor is called

print("an contains",an)

#Constructor 

#In object oriented programming, a constructor in a class is a special
#block of statements called when an object is created.

#Many Instances:

#We can create lots of objects- the class is the template for the object
#We can store each distinct object in its own variable
#We call this having multiple instances of the same class
#Each instance has its own copy of the instance variables
#Constructors can have additional parameters.
#These can be used to set up instance variables for the particular instance of the class(i.e., for the particular object).
class PartyAnimal:
    x=0 #data member
    name="" #data member

    def __init__(self, z): #this is a constructor
        self.name=z
        print(self.name,"constructed")

    def party(self):    #this is a method/member function
        self.x=self.x+1
        print(self.name,"party count",self.x)

s=PartyAnimal("Sally")
s.party()

j=PartyAnimal("Jim")
j.party()
s.party()
