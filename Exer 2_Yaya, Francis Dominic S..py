from math import*
x=input("Enter a number: ")
factorial = 1
for i in range(1,x+1):
    factorial = factorial*i
print "The factorial of", x, "is", factorial
