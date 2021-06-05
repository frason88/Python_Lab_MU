# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:06:08 2021

@author: jkfra
"""

class Cab:
    
    #Initialise variables for first iteration
    numberofcabs  = 0
    numpassengers = 0

    def __init__(self,driver,kms,places,pay,passengers):
        self.driver = driver
        self.running = kms
        self.places = places
        self.bill = pay
        Cab.numberofcabs  =  Cab.numberofcabs + 1
        Cab.numpassengers =  Cab.numpassengers + passengers

    #Returns price of cab fare per km
    def rateperkm(self):
        return self.bill/self.running
        
    #Returns number of cabs running         
    @classmethod
    def noofcabs(cls):
        return cls.numberofcabs

    #Returns average number of passengers travelling in a cab
    @classmethod
    def avgnoofpassengers(cls):
        return int(cls.numpassengers/cls.numberofcabs)

firstcab  = Cab("Ramesh", 80, ['Delhi', 'Noida'], 2200, 3)
secondcab = Cab("Suresh", 60, ['Gurgaon', 'Noida'], 1500, 1)
thirdcab  = Cab("Dave", 20, ['Gurgaon', 'Noida'], 680, 2)
  



"""

Methods:

In python, there are three types of methods which are Instance, 
Class and Static.

Instance takes self as the first argument. They are also called Object or regular method. 
It's the same method which we have learnt so far in previous sections.
Class takes cls as the first argument. cls refers to class. 
To access a class variable within a method, we use the @classmethod decorator, 
and pass the class to the method Staticdoesn't take anything as the first argument. 
It has limited uses which are explained in the latter part of this article.


How Instance and class methods are different?
Instance method can access properties unique to a object or instance. Whereas Class method is used when you want to access a property of a class, and not the property of a specific instance of that class. The other difference in 
terms of writing style is that Instance method take self as a first parameter whereas Class method takes cls as a first parameter.
In the example below, we are creating class for cab. Both Cab and taxi means the same thing. 
Attributes or properties of cab is driver name, number of kilometers run by a cab, Pick-up and drop location, cab fare and number of 
passengers boarded cab.

Here we are creating 3 methods : rateperkm, noofcabs, avgnoofpassengers. 
First one is instance method and other two are class methods.

rateperkm returns price of cab fare per km which is calculated by dividing total bill by no. of 
kms cab traveled.
noofcabs returns number of cabs running. Think about cab agency which owns many cabs and wants to
know how many cabs are busy
avgnoofpassengers returns average number of passengers traveling in a car. 
To calculate average, it takes into account all the cabs running and number of passengers in each 
cab.



"""











