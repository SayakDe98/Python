#class is a reserved word.
#Each PartyAnimal object has a bit of code.
#Tell an object to run the party() code within it.
#This is the template for making PartyAnimal objects.
#Each PartyAnimal object has a bit of data.
#Construct a PartyAnimal object and store in an PartyAnimal.party(an)

class PartyAnimal:
    x=0

    def party(self):
        self.x=self.x+1
        print("So far",self.x)

an=PartyAnimal()    #Assigning PartyAnimal into an

#Calling the PartyAnimal() three times
an.party()  
an.party()
an.party()

#Playing with dir() and type()
#A Nerdy Way to Find Capabilities
#The dirt() command lists capabilities
#Ignore the ones with underscores- these are used by Python itself
#The rest are real operations that the object can perform
#It is like type() -it tells us something "about" a variable

x=list()    #there is already a list class in python and when we are assigning an empty list into x
print(type(x))  

print(dir(x))

print("Type",type(an))
print("Dir",dir(an))    #we will find party and x by doing this.