a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",""] #后面参数设定的原因，n要到达15，所以需要a[15]
b = ""
n = 0
sequence = b + a[n] + b
while n < 15:
    sequence = b + sequence + b
    n = n + 1
    b = a[n]
    print(sequence)