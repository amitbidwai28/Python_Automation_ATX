def factorial():
    fact = int(input("Enter the no. for factorial: "))
    num = 1
    for i in range(1, fact + 1):
        num = num * i
    print("Factorial of the given no. is", num)


factorial()
