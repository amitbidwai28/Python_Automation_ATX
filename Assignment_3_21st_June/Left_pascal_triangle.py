num1 = 5
for i in range(num1-1):
    for j in range(i, num1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print("\r")
num = 5
for i in range(num):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, num):
        print("*", end=" ")
    print("\r")