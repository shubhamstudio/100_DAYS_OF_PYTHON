# name = input("Enter your name: ")
# age = input("What's your age: ")
# # print("Hello", name,",you are", age, "years old!")
# print(f"Hello {name}, you are {age} years old")

# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# print("The sum of a and b is: ", a+b) #sum
# print("The difference of a and b is: ", a-b) #difference
# print("The product of a and b is: ", a*b) #product
# print("The quotient of a and b is: ", a/b) #quotient

# num1 = int(input("Enter first value in int: "))
# num2 = int(input("Enter second value in int: "))
# num3 = float(input("Enter third value in float: "))
# average = (num1+num2+num3)/3
# print("The average of all three numbers are: ", sum)

# user_input = input("Enter a value: ")
# val_int = int(user_input)
# val_float = float(user_input)
# val_string = str(user_input)
# print(type(val_int), val_int)
# print(type(val_float), val_float)
# print(type(val_string), val_string)

# print(10+3*2**2)

# num1 = input("Enter first value: ")
# num2 = input("Enter second value: ")
# num1, num2 = num2, num1
# print("The num1 is:", num1)
# print("The num2 is:", num2)

# enter_temp = float(input("Enter the temperature in Celsius: "))
# fahrenheit_temp = (enter_temp*(9/5))+32
# print("Temperature in fahrenheit is:", fahrenheit_temp)

'''To convert farhenheit to celsius
conversion = (farhenheit - 32) * 5/9
'''

num = float(input("Enter a value: "))

int_part = int(num)

float_part = round(num - int_part, 3)

print(type(int_part), int_part)
print(type(float_part), float_part)

