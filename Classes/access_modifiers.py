# Protected Access Modifier:
# The members of a class that are declared protected are only accessible
# to a class derived from it. Data members of a class are declared protected
# by adding a single underscore ‘_’ symbol before the data member of that class.
# # super class
# class Student:
#     # protected data members
#     _name = None
#     _roll = None
#     _branch = None
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         self._name = name
#         self._roll = roll
#         self._branch = branch
#
#     # protected member function
#     def _displayRollAndBranch(self):
#         # accessing protected data members
#         print("Roll: ", self._roll)
#         print("Branch: ", self._branch)
#
#
# # derived class
# class Geek(Student):
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         Student.__init__(self, name, roll, branch)
#
#         # public member function
#
#     def displayDetails(self):
#         # accessing protected data members of super class
#         print("Name: ", self._name)
#
#         # accessing protected member functions of super class
#         self._displayRollAndBranch()
#
#
# # creating objects of the derived class
# obj = Geek("R2J", 1706256, "Information Technology")
#
# # calling public member functions of the class
# obj.displayDetails()

# Private Access Modifier: The members of a class that are
# declared private are accessible within the class only,
# private access modifier is the most secure access modifier.
# Data members of a class are declared private by adding a
# double underscore ‘__’ symbol before the data member of that class.
# # program to illustrate private access modifier in a class
#
#
# class Geek:
#     # private members
#     __name = None
#     __roll = None
#     __branch = None
#
#     # constructor
#     def __init__(self, name, roll, branch):
#         self.__name = name
#         self.__roll = roll
#         self.__branch = branch
#
#     # private member function
#     def __displayDetails(self):
#         # accessing private data members
#         print("Name: ", self.__name)
#         print("Roll: ", self.__roll)
#         print("Branch: ", self.__branch)
#
#     # public member function
#     def accessPrivateFunction(self):
#         # accesing private member function
#         self.__displayDetails()
#
#     # creating object
#
#
# obj = Geek("R2J", 1706256, "Information Technology")
#
# # calling public member function of the class
# obj.accessPrivateFunction()



# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj, ccode, new_proj=None):
        self.name = name  # name(name of company) is public
        self._proj = proj  # proj(current project) is protected
        self.new_proj = new_proj
        self.ccode = ccode

    # public function to show the details
    def show(self):
        print("The code of the company is = ", self.ccode)


# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj, cCode):
        # calling parent class constructor
        Company.__init__(self, cName, proj, cCode)
        self.name = eName  # public member variable
        #self._proj = proj  # private member variable
        self.__sal = sal  # private member variable

    # public function to show salary details
    def show_sal(self):
        print("The salary of ", self.name, " is ", self.__sal, )


# creating instance of Company class
c = Company("Stark Industries", "Mark 3", ccode='STI')
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name, c._proj, c.ccode)

print("Welcome to ", c.name)
print("Here ", e.name, " is working on ", e._proj)

# only the instance itself can change the __sal variable
# and to show the value we have created a public function show_sal()
e.show_sal()
e.show()