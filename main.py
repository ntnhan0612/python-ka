# Calling module module_reference.a from main module
# There is no need to use sys module, because main module was placed at root package level
from module_reference.a import A

class D:
    def function_c(self):
        print("This is function_d from class D")

A().function_a()