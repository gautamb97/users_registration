import re


class Registration:
    print("Welcome for Registration")
    name_validation = "^[A-Z]{1}[a-z]{2,10}"
    pat = re.compile(name_validation)
    def firstname(self):
        '''takes input from user and check validation of first name it includes at least one uppercase letter'''
        firstName = input("Enter your first name: ")
        mat = re.search(Registration.pat,firstName)
        if mat:
            return firstName
        else:
            return "invalid first name"

    def lastName(self):
        '''takes input from user and check validation of last name it includes at least one uppercase letter'''
        lastName = input("Enter your last name: ")
        matchingForLastName = re.search(Registration.pat,lastName)
        if matchingForLastName:
            return lastName
        else:
            return "invalid last name"

    def email(self):
        '''takes input from user and check email validation includes domain and valid format'''
        email = input("Enter your email address: ")
        patternCheckingForEmail = "^[a-z]*\@[a-z]*\.(com|org|com\.co|com\.edu)"
        matchingForEmail = re.search(patternCheckingForEmail,email)
        if matchingForEmail:
            return email
        else:
            return "invalid email address"

    def mobilenumber(self):
        '''takes input from user for his/her mobile number and checks validity'''
        mobileNumber = input("Enter your mobile number: ")
        patternCheckingForMobileNumber = "^(\+91)?[6-9]{1}[0-9]{9}$"
        matchingForMobileNumber = re.search(patternCheckingForMobileNumber,mobileNumber)
        if matchingForMobileNumber:
            return mobileNumber
        else:
            return "invalid mobile number"

    def passwordruleone(self):
        '''takes input from user for password and checks whether it is of 8 character and validate'''
        eightCharacter = input("Enter your password: ")
        patternCheckingForEightCharacter = "[a-z]{8,}"
        matchingForEightCharacter = re.search(patternCheckingForEightCharacter,eightCharacter)
        if matchingForEightCharacter:
            return eightCharacter
        else:
            return "invalid password"

if __name__== '__main__':
    registration = Registration()
    (registration.firstname())
    (registration.lastName())
    (registration.email())
    (registration.mobilenumber())
    (registration.passwordruleone())