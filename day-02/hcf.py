
print("--------HCF CACLULATOR------")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Selection: Find the smaller number
if num1 < num2:
    factor = num1
else:
    factor = num2

# Iteration: Find the HCF
while num1 % factor != 0 or num2 % factor != 0:
    factor = factor - 1 

# Output
print("The Highest Common Factor is:", factor)