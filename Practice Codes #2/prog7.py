#  Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
total = 0

for i in range (10):
    num = float(input(f"Enter number{i+1}:"))
    
    if num % 2 == 0:
        total += 1
    
print(f"The number of even numbers are: {total}")