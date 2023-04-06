# Question: Build a simple calculator that prompts the user to input the kind of arithmetic
# operation it wants to perform and also the values

# Prompt the user to input the arithmetic operation
operation = input("Which Arithmetic Operation:  ")

# Prompt the user to input the values
value1 = float(input("Enter the first value:  "))
value2 = float(input("Enter the second value: "))

# Perform the arithmetic operation chosen by the user
if operation == "+":
    answer = value1 + value2
elif operation == "-":
    answer = value1 - value2
elif operation == "*":
    answer = value1 * value2
elif operation == "/":
    answer = value1 / value2
else:
    print("Invalid operation.")
    exit()

# Print the answer
print("The result of the operation is:", answer)