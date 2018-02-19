print "Each game console cost 22000" 
money = input("How much money do you have in your account now? Php ")
y=(money)/22000
print "The number of game consoles with a price of Php 22000 you can buy is ", y
n = (money) - y*22000
print "After buying the consoles, you will have", n,"pesos left on your account"
e = 22000 - n
print "You will need an additional amount of at least", e,"pesos to buy a new console"
