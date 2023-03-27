def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1	
    while b < n:
        print(b, end =" ")
        a, b = b, a+b
'''Write a python program to define a module to find Fibonacci Numbers and import the
module to another program'''
#import fibonacci module
import fibonacci 
num=int(input("Enter any number to print Fibonacci series "))
fibonacci.fib(num)
