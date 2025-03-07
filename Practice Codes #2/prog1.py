#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

num1 = float(input("Input Number 1: "))
num2 = float(input("Input Number 2: "))

if num1 > num2:
    print(f"The smaller num is: {num2}")
elif num1 < num2:
    print(f"The smaller num is: {num1}")
else:
    print("The numbers are equal")
