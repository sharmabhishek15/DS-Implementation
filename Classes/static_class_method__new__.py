class Example:
    def __new__(self):
        return 'studytonight'

# creating object of the class Example
mutantObj = Example()

# but this will return that our object
# is of type str
print (type(mutantObj))



class Example2:
    myVariable = "some value";

simpleObj = Example2()
print (type(simpleObj))