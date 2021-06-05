# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:28:33 2021

@author: jkfrason

Aim: Creating user defined multithreaded application with thread synchronization and deadlocks
"""
#Application on Multithreading sync with deadlock on a typical webpage scenario

import threading #module
import time #sync with time for deadlock 


class myThread1(threading.Thread): #creating subclass from main class thread
    def __init__(self, threadId, name, count): #method 
        threading.Thread.__init__(self) #parent-constructor method called 
        self.threadId = threadId
        self.name = name
        self.count = count #In our example we will count on numbers so we use count

    def run(self):          #To run the thread (method)
        print("Starting: " + self.name + "\n")
        threadLock.acquire()   #lock the thread so that no other thread run unless this thread finishes
        print_time(self.name, 1,self.count)     #giving the delay of 1'sec
        threadLock.release()    #To release the lock of the thread 
        print("Exiting: " + self.name + "\n")   #Done with thread

class myThread2(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        threadLock.release()
        print_time(self.name, 1,self.count)
        print("Exiting: " + self.name + "\n")


def print_time(name, delay, count):
    while count:
        time.sleep(delay) #delay/sleep by
        print ("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n") #time.ctime giving current time
        count -= 1  #for counting down


threadLock = threading.Lock()

thread1 = myThread1(1, "Payment", 5) #waiting for 5 sec
thread2 = myThread2(2, "Sending Email", 10) #waiting for 10 sec, will be executed after payment
thread3 = myThread2(3, "Loading Page", 3) #waiting for 3 sec will be executed after the sending email

#Execution of thread

thread1.start()
thread2.start()
thread3.start()
thread1.join() #To wait fot the thread to finish before exiting the program
thread2.join()
thread3.join()
print("Done main thread")  

