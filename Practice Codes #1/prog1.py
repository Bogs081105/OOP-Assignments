#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
num_1 = float(input("Input Number 1: "))
num_2 = float(input("Input Number 2: "))
if num_1 > num_2:
    print(f"The greater number is: {num_1}")
elif num_2 > num_1:
    print(f"The greater number is: {num_2}")
elif num_1 == num_2:
    print("The numbers are equal")