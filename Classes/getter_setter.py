class Employee:

    def __init__(self, fName, lName, resigned=False):
        self.fName = fName
        self.lName = lName
        self.resigned = resigned
        self.email = (self.fName, self.lName)

    #getter
    def get_email(self):
        #print("Getting Email")
        self.email = (self.fName, self.lName)
        return self._email

    #setter
    def set_email(self, val):
        #print("Setting Email")
        a,b = val
        self._email = a + '.' + b + '@gmail.com'

    email = property(fget=get_email, fset=set_email)

    def __str__(self):
        return 'Object of {} {}'.format(self.fName, self.lName)

obj = Employee('abhishek', 'sharma')
print(obj.fName, obj.lName)
print(obj.email)
obj.fName = 'Change'
print(obj.fName, obj.lName)
print(obj.email)
print('='*25)


class Employee2:

    def __init__(self, fName, lName, resigned=False):
        self.fName = fName
        self.lName = lName
        self.resigned = resigned
        self.email = (self.fName, self.lName)

    #getter
    @property
    def email(self):
        #print("Getting Email")
        self.email = (self.fName, self.lName)
        return self._email

    #setter
    @email.setter
    def email(self, val):
        #print("Setting Email")
        a,b = val
        self._email = a + '.' + b + '@gmail.com'

    #email = property(fget=get_email, fset=set_email)

    def __str__(self):
        return 'Object of {} {}'.format(self.fName, self.lName)

print('------------@property decorator----------------------------')
obj = Employee('Property', 'Decorator')
print(obj.fName, obj.lName)
print(obj.email)
obj.fName = 'Change'
print(obj.fName, obj.lName)
print(obj.email)
print('='*25)