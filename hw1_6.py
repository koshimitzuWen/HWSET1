x = 0
y = 0
z = 0

for x in range(0, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            if 100 * x + 10 * y + z == x*x*x + y*y*y + z*z*z and (100 * x + 10 * y + z) >=100:
                print(str(x*x*x + y*y*y + z*z*z))
            else:
                z = z + 1
        y = y + 1
    x = x + 1
