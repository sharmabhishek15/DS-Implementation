# Corner Cases: When Destructor doesn't behave well
# As we already mentioned in the start that using __del__ is not a full proof solution to perform the final clean up for an object which is no longer required.
#
# Here we have discussed two such situations where __del__ function behaves absurd.
#
# 1. Circular Referencing
# Circular referencing refers to a situation where two objects refers to each other. In such a case when both of these objects goes out of reference, python is confused to destroy which object first, and to avoid any error, it doesn't destroy any of them.
#
# Here is an example to demonstrate circular referencing,

class Foo():
    def __init__(self, id, bar):
        self.id = id;
        # saving reference of Bar object
        self.friend = bar;
        print('Foo', self.id, 'born');

    def __del__(self):
        print('Foo', self.id, 'died');


class Bar():
    def __init__(self, id):
        self.id = id;
        # saving Foo class object in variable
        # 'friend' of Bar class, and sending
        # reference of Bar object for Foo object
        # initialisation
        self.friend = Foo(id, self);
        print('Bar', self.id, 'born')

    def __del__(self):
        print('Bar', self.id, 'died')


b = Bar(12)