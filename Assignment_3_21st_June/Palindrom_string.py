def palindrome_string(name1):
    sting_name = "".join(reversed(name1))
    if name1 == sting_name:
        print("String in palindrom")
    else:
        print("Not palindrome")


name = str(input("Enter the string: ").lower())
palindrome_string(name)