'''
Decorator : decorators are a powerful and flexible way to modify or extend the behavior of functions or
methods without directly altering their source code.
They are essentially higher-order functions that take another function as an argument and
return a new function, typically with enhanced or modified functionality
'''
from time import time

#creating decorator function to measure the execution time
def measure_time(func):
    def wrapper(*args):
        start_time = time()
        func(*args)
        print(f"Total execution time is - {time()-start_time} in seconds")
    return wrapper

#creating another decorator function to greet the every cycle of the whole day
def greeting(func):
    def wrapper(*args):
        print("Hello ,",end='')
        func(*args)
    return wrapper

#original functions which calls decorators
@greeting
@measure_time
def morning(name):
    print(f" Good Morning - {name}")

@greeting
@measure_time
def afternoon(name):
    print(f" Good Afternoon - {name}")


@greeting
@measure_time
def night(name):
    print(f" Good Night - {name}")

morning("Girish")
afternoon("Harish")
night("Suresh")

#output
'''
/usr/bin/python3.10 /home/giri/Desktop/Programs/new_assignment/decorators.py 
Hello , Good Morning - Girish
Total execution time is - 8.344650268554688e-06 in seconds
Hello , Good Afternoon - Harish
Total execution time is - 5.4836273193359375e-06 in seconds
Hello , Good Night - Suresh
Total execution time is - 4.76837158203125e-06 in seconds
'''