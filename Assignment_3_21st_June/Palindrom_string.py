def palindrom_string(name):
    sting_name = "".join(reversed(name))
    print(sting_name)
    if name == sting_name:
        print("String in palindrom")
    else:
        print("Not palindrome")


#
name = str(input("Enter the string: "))
palindrom_string(name)
