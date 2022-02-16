# from a import A
import a
class B:
    def function_b(self):
        print("This is function_b from class B")

class_instance = B()
class_instance.function_b()

a.A().function_a()