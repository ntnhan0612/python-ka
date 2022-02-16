# - module_reference
    # - a.py (module a)
    # - b.py (module b)
# - module_reference_2
    # - c.py (module c)

# Calling module module_reference.a from folder module_reference_2.c

import sys
sys.path.insert(0, '/home/cimb/nhan/python-projects/python-ka/module_reference')
from a import A

class C:
    def function_c(self):
        print("This is function_b from class C")

A().function_a()