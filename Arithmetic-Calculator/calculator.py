# Python arithmetic calulator

# String concatenation
operator = input("Enter an operator (+ - * /): ")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if operator == "+":
    result = number1 + number2
    print(round(result))
elif operator == "-":
    result = number1 - number2
    print(round(result))
elif operator == "*":
    result = number1 * number2
    print(round(result))
elif operator == "/":
    result = number1 / number2
    print(round(result))
else:
    print(f"{operator} is not a valid operator")