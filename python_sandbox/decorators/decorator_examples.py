"""
The only constraint on the result of a decorator is that it be callable, so it can properly
replace the decorated function.
"""

def decorator_example(f):
    def new_f():
        print "Entering", f.__name__
        f()
        print "Exited", f.__name__
    return new_f

@decorator_example
def test_function1():
    print "Inside test_function1"
    
@decorator_example
def test_function2():
    print "Inside test_function2"
    
if __name__ == "__main__":
    """
    Should print:
    Entering test_function1
    Inside test_function1
    Exited test_function1
    Entering test_function2
    Inside test_function2
    Exited test_function2
    new_f
    """
    test_function1()
    test_function2()
    print test_function1.__name__