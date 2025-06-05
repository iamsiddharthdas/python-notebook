'''
Process - example - Running Google Chrome
Thread - example - Running multiple tabs in Google Chrome

Concurrency - Concurrency is about dealing with multiple tasks at once, 
where tasks can start, run, and complete in overlapping time periods.
(example - multithreading)

Parallelism - It is about doing multiple tasks at the exact same time, executed one by one.
(example - normal coding in Python)

'''

import threading 

def fun():
    for i in range(10):
        print("Hum honge kaamyaab")
        
def raju():
    for i in range(10):
        print("Aaj nahi kal padhenge")
        
fun()
raju() 


t1 = threading.Thread(target=fun) # creating a thread
t2 = threading.Thread(target=raju)

t1.start()
t2.start()

'''
Output: (it changes every time)

Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaabAaj nahi kal padhenge
Aaj nahi kal padhenge

Aaj nahi kal padhenge
Hum honge kaamyaab
Aaj nahi kal padhenge
Aaj nahi kal padhenge


'''

# Sleep

import threading 
import time

def fun():
    for i in range(10):
        time.sleep(0.5) # given priority to this thread by giving more time (0.5 > 0.4)
        print("Hum honge kaamyaab")
        
def raju():
    for i in range(10):
        time.sleep(0.4)
        print("Aaj nahi kal padhenge")
        
fun()
raju() 


t1 = threading.Thread(target=fun) # creating a thread
t2 = threading.Thread(target=raju)

t1.start()
t2.start()

'''
Output:

Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Hum honge kaamyaab
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Hum honge kaamyaab
Aaj nahi kal padhenge
Hum honge kaamyaab
Aaj nahi kal padhenge
Hum honge kaamyaab
Aaj nahi kal padhenge
Hum honge kaamyaab
Aaj nahi kal padhenge
Aaj nahi kal padhenge
Hum honge kaamyaab
Aaj nahi kal padhenge
Hum honge kaamyaab
Aaj nahi kal padhenge
Hum honge kaamyaab
Aaj nahi kal padhenge
Hum honge kaamyaab
Aaj nahi kal padhenge
Hum honge kaamyaab
Hum honge kaamyaab

'''

# using oops concept 

'''using single class'''

import threading

class A:
    
    def fun(self):
        for i in range(10):
            print("Hum honge kaamyaab")
        
    def raju(self):
        for i in range(10):
            print("aaj nahi kal padhenge")
            
obj = A()

t1 = threading.Thread(target=obj.fun) 
t2 = threading.Thread(target=obj.raju)

t1.start()
t2.start()


'''using two classes'''

import threading

class A(threading.Thread):
    def run(self):
        for i in range(10):
            print("Aaj nahi kal padhenge")
            
class B(threading.Thread):
    def run(self):
        for i in range(10):
            print("Aaj nahi kal padhenge")
            
obj = A()
obj2 = B()

obj.start()
obj2.start()

