number = int(input("print the size of Christmas tree: ")) #代表树干部分一共有多少行
space = number-1  #代表*左右两侧对称空格的数量
asteroid = 1  #代表每行*的数量

# 树冠部分
for x in range(0, number):                  #这个循环来控制行数
    for x in range(0, space):               #先放了一堆space
        print(" ",end = " ") 
    for x in range(0, asteroid):            #再放了一堆*
        print("*",end = " ")
    for x in range(0, space):               #再放一堆对称的space
        print(" ",end = " ")
    asteroid = asteroid + 2                 #上面一排放好了，所以重新改*的数量
    space = space - 1                       #和space的数量
    print(end = "\n")                       #换行。有什么更好的方式吗OTZ

# 树干部分
half_number = int(number/2)
for x in range(0, half_number):
    for x in range(0, number - 1):          #先放了一堆space
        print(" ",end = " ")
    print("*")

