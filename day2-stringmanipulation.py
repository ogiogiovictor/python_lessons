################# Python Primitive Data Type########################
print("Hello"[0]) ## getting the first character from the string. This is called subscripting. can start from 0, 1,2, 3 ...end
print(124_356_567_000)

################# Type Error, Type Checking and Type Conversion #######################
num_char = 5
print(type(num_char))  # Type Chechking

################ Type Conversion ############
new_num_char = str(num_char)
print(type(new_num_char))

two_digit = "39"[0]
last_digit = "39"[1]

print(int(two_digit) + int(last_digit))

#### PEMDAS #######
# Parentheses
# Exponents
# Multiplication
# Division
# Addition
# Substraction

#################### BODY MASS INDEX CALCULATION #####################
height = input()
weight = input()

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2
print(bmi)


#################### ROUND FUNCTION #####################
print(round(8 / 3, 2))
print(897 // 3) ## The floor division

#################### F STRINGS #####################
score = 5
height = 1.8
isWinning = True
print(f'your socre is {score} and height is {height} and wining is {isWinning}')

################### CALCULATE LIFETIME WEEKS ##############################
age = input()
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} left")

################### TIP CALCULATOR ##############################
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill?"))

bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)
bill_per_person = round(bill_with_tip / people, 2)  #"{:2f}.format(bill_per_person)"
print(f" Each person will pay {bill_per_person}")