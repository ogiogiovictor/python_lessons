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