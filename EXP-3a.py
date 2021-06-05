# -*- coding: utf-8 -*-
"""
@author: jkfrason
"""


class Employee():
    'Common base class for all employees'
    empCount = 0
    
    #constructor 
    def __init__(self, eid, name, salary, did):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.did = did
        Employee.empCount += 1
        
     #instance method 
    def displayEmployee(self):
        print("eid : ", self.eid,", Name : ", self.name,  ", Salary: ", self.salary,  ", did: ", self.did)
    
    @staticmethod
    def info(msg):
        print("Total Employee %d" % Employee.empCount)

"This would create first object of Employee class"
emp1 = Employee(1,"Millena", 2000,10)
"This would create second object of Employee class"
emp2 = Employee(2,"Frason", 4000,20)
emp1.displayEmployee()
emp2.displayEmployee()

Employee.info("calling the static method")



