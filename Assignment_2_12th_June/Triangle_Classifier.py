def Classifir():
    side1 = float(input("Enter the first side"))
    side2 = float(input("Enter the second side"))
    side3 = float(input("Enter the third side"))
    if (side1 == side2 and side2 == side3 and side3 == side1):
        print("Triangle is equilaterl")
    elif (side1 == side2) or (side2 == side3) or (side3 == side1):
        print("Triangle is isosceles")
    else:
        print("Triangle is scalene")


Classifir()
