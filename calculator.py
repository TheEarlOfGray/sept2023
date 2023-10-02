num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
print("Add: +\nSubtract: -\nMultiply: *\nDivide: /\nSquare: S")
op = input("Please enter the operation to perform: ")

if op == "+":
    res = num1 + num2
    print(res)
elif op == "-":
    res = num1 - num2
    print(res)
elif op == "*":
    res = num1 * num2
    print(res)
elif op == "/":
    res = num1 / num2
    print(res)
elif op == "S":
    res = num1 ** num2
    print(res)
else:
    print("Not a valid operation, try again.")