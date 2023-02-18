#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#
from pprint import pprint

# import inspection module
import inspect

# Supercalss, also called Parent class
class Vehicle():
    def __init__(self, bodystyle):       # the function that python calls when the object is being created
        self.bodystyle = bodystyle       # defined the property on the class of the value which is passed in when the class is created
    
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

    def insurance(self,age):
        self.age = age
        if age <15:
            self.insurancestate = "insured"
            self.yearlyinsurance = 100*age*age*age/3
        else:
            self.insurancestate = "not insured"

    def blacha(self, color, polish):
        self.color = color
        self.polish = polish

    

# Two subclasses, which both inherit from the vehicle and have their own properties
class Car(Vehicle):                     # Vehicle - superclass of a class Car
    def __init__(self, enginetype):
        super().__init__("Car")         # initialize bodystyle property in the superclass (parent class)
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype 

    # def __init__(self, enginetype, color, polish):
    #     super().__init__("Car")         # initialize bodystyle property in the superclass (parent class)
    #     self.wheels = 4
    #     self.doors = 4
    #     self.enginetype = enginetype 
    #     self.color = color
    #     self.polish = polish

    def blacha(self, color, polish):
        super().blacha(color, polish)
        if (polish):
            print("This", self.bodystyle, "is", self.color, "and polished")
        else:
            print("This", self.bodystyle, "is", self.color, "and unpolished")

    def drive(self, speed):         # drive method
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

    def insurance(self, age):
        super().insurance(age)
        if age < 15:
            print("Age of the", self.enginetype, "car is", self.age,". This car is", self.insurancestate, ". Yearly insurance to be paid is", self.yearlyinsurance, "zloty")
        else:
            print("Age of the", self.enginetype, "car is", self.age,". This car is", self.insurancestate, ". No yearly insurance is paid")
        

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")  # we dont have to def self paratemer, it is implied in python
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype 

    def drive(self, speed):         # drive method
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)

    def insurance(self, age):
        super().insurance(age)
        if age < 15:
            print("Age of the", self.enginetype, "motorcycle is", self.age,". This motorcycle is", self.insurancestate, ". Yearly insurance to be paid is", self.yearlyinsurance, "zloty")
        else:
            print("Age of the", self.enginetype, "motorcycle is", self.age,". This motorcycle is", self.insurancestate, ". No yearly insurance is paid")
        

# Once we have classes defined we can create specific objects of those types
# Let's create a couple of class and motorcycles:


#car1 = Car("gas", "blue", True)
car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas",True)

# Now that we defined these classes and we've initialized them, we can access their properties with dot notation
print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)

car1.insurance(16)
car1.insurance(9)
mc1.insurance(3)

car1.blacha("red", True)
car2.blacha("black", False)

print(vars(car1))   
print(vars(car2))
print(vars(mc1))

pprint(dir(car1))

# using inspect module, to print all the attributes of an object you can use 'getmembers()'
pprint(inspect.getmembers(car1))