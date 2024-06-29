class employee_class:

    def __init__(self, name1, sal, role_dept1):
        self.name = name1
        self.__sal = sal
        self.role_dept = role_dept1

    def display_details(self):
        print("The name of the employee is: ", self.name)
        print("To Check the salary authenticate yourself, enter the passcode: ")
        usr_entry = input("Enter the passcode: ")
        if usr_entry == "1234":
            print("The Salary is: ", self.__sal)
        else:
            print("You are not valid user")

    def internal_method(self):
        pass

    def __update_salary(self):
        new_amnt = input("Enter the amount to be added")
        self.__sal += int(new_amnt)
        print("Salary has been updated", self.__sal)

    def auth_user(self, auth, passcode):
        if auth:
            self.__update_salary()
        else:
            print("You have not authenticated yourself")


emp_obj2 = employee_class(name1="Sumit", sal=6000, role_dept1="SSEE")
emp_obj2.display_details()
pass_code = input("Enter the passcode: ")
if pass_code == "1234":
    emp_obj2.auth_user(True, pass_code)
else:
    emp_obj2.auth_user(False, pass_code)

# emp_obj.auth_user(True, pass_code)
