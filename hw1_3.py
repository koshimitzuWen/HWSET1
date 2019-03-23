number = int(input("Please input an integer: "))
x = 0
sum = 0
for n in range(0, number + 1):
    sum = sum + x
    x = x + 1
print(sum)