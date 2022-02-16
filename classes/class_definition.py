# There is no limitation number of Class definition in a module (py file)

# class definition MyClass
class MyClass:
    def my_function(self):
        print("Passed")

class_instance = MyClass()
class_instance.my_function()


# class definition MyClass2
class MyClass2:
    #__init__ is default constructor of Class in Python, with default "self" argument
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def my_function2(self):
        print("My name is " + self.fname + " " + self.lname)

class_instance2 = MyClass2("Nhan", "Nguyen")
class_instance2.my_function2()