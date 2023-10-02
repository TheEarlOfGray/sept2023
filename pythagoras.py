control = input("Find the length of A, given B and C: 1\nFind the length of B, given A and C: 2\nFind the length of C, given A and B: 3")

if control == "1":
    num1 = float(input("Please enter the length of side B"))
    num2 = float(input("Please enter the length of side C"))
    res = ((num2**2) - (num1**2)) ** 0.5 
    print(res)
elif control == "2":
    num1 = float(input("Please enter the length of side A"))
    num2 = float(input("Please enter the length of side C"))
    res = ((num2**2) - (num1**2)) ** 0.5 
    print(res)
elif control == "3":
    num1 = float(input("Please enter the length of side A"))
    num2 = float(input("Please enter the length of side B"))
    res = ((num1 ** 2) + (num2 ** 2)) ** 0.5
    print(res)