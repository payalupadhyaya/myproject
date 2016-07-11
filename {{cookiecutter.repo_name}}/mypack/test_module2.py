from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division
from mypack.packmodule import module3

def cust_print():
    print("Hi Hello")

def test_mypackage():
    cust_print()
    module3()
    print("Test ended")




