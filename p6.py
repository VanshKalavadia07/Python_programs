# Program to find the greatest among three numbers using nested if

# Take three numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Main comparison logic using nested if
if num1 >= num2:
    # If num1 is greater than or equal to num2, compare num1 with num3
    if num1 >= num3:
        greatest = num1
    else:
        greatest = num3
else:
    # If num1 is not greater than num2, it means num2 is larger. 
    # Now, compare num2 with num3
    if num2 >= num3:
        greatest = num2
    else:
        greatest = num3

# Display the result
print(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")