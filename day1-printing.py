print("Welcome this the Day1 of Python 100 Days of Code Challenge!")
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")


##################################LINE BREAK ######################
print("Adding a backslash\nHello World")

######################## STRING CONCATENATION ####################
print("Hello " + "Angela")

############## INPUT FUNCTION #####################################
input("What's your name? ")
input("Hello " + input("Who are u? "))

#len() tells you how many characters is in a particular string
name = len(input("Len Function Tells me the Length of a String? "))
print(name)

################# SWITCH RULE VARIABLES ###############
a = input("Assembly")
b = input("Basic")

c = a
a = b
b = c

print("a " + a)
print("b " + b)

################# DAY 1 FINAL PROJECT ########################
print("Welcome to the band name Generator")
city = input("What City Did You Grow Up? \n")
pet = input("What is the name of your pet?\n")

brand = print("Your City is " + city + "Your Pet Name is " + pet + "\n")
print(brand)