#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

total = 0

for i in range (10):
    num = float(input(f"Enter number{i+1}:"))
    total -= num
print (f"The total of the numbers are {total}")