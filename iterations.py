total = 0
control = True

while control:
    total = int(input("Enter a number: "))

    if total == 21:
        continue

    print(total)
    control = bool(input("Get another number? "))

print(f"Total: {total}")