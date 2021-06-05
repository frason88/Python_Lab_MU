# -*- coding: utf-8 -*-
"""
@author: jkfrason
"""
      
class Vehicle:

    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"        
    
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
        
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

class taxi(Vehicle):
    def seating_capacity(self, capacity=3):
        return super().seating_capacity(capacity=3)

School_bus = Bus("Volvo Bus", 180, 12,50)
print(School_bus.seating_capacity())
print("Total Bus fare is:", School_bus.fare())

print("\n--------------------------------------------------------------------\n")

taxi = taxi("Taxi", 280, 22,3)
print(taxi.seating_capacity())
print("Total taxi fare is:", taxi.fare())









