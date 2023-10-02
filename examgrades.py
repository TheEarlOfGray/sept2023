mark = int(input("Please enter the mark: "))
level = int(input("Please enter the students level: "))

if level == 1:
    if mark in range(1, 101):
        if mark > 70:
            print("Distiction")
        elif mark > 60:
            print("Merit")
        elif mark >= 50:
            print("Pass")
        else:
            print("Fail!")
    else:
        print("Invalid mark, please try again.")
elif level == 2:
    if mark in range(1, 101):
        if mark > 66:
            print("Distiction")
        elif mark > 50:
            print("Merit")
        elif mark >= 40:
            print("Pass")
        else:
            print("Fail!")
    else:
        print("Invalid mark, please try again.")
else:
    print("Not a valid level try again.")

