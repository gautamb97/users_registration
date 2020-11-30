import re


class Registration:
    print("Welcome for Registration")
    name_validation = "^[A-Z]{1}[a-z]{2,10}"
    def firstname(self):
        '''takes input from user and check validation of first name it includes at least one uppercase letter'''
        firstName = input("Enter your first name: ")
        pat = re.compile(Registration.name_validation)
        mat = re.search(pat,firstName)
        if mat:
            return firstName
        else:
            return "invalid first name"

if __name__== '__main__':
    registration = Registration()
    (registration.firstname())

