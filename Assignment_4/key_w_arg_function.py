def bank_account_details(**detail):
    print("\n", "Details are: ")
    for key, value in detail.items():
        print("{} is {}".format(key, value))


bank_account_details(name="Amit", bank_acc=1234, city="Pune")
bank_account_details(name="Sumit", bank_acc=4321, city="Delhi")
bank_account_details(name="Arab", bank_acc=3421, city="Karachi")
