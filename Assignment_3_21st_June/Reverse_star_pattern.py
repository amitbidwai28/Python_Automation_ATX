def star_pt(num):
    for i in range(num):
        for j in range(i, num):
            print("*", end=" ")
        print("\r")


val = int(input("Enter the value: "))
star_pt(val)
