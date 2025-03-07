#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
quotient = num1 // num2

print(f"{num1} / {num2} = {quotient}")