# 100, += (N/100)*10, counter += 1, while N <= 1000.

num = int(input("Enter a starting value: "))

counter = 0

target = int(input("Enter a target value: "))

interest = int(input("Enter an interest amount: "))

while num <= target:
    num += num / 100 * interest
    counter += 1

print(counter)