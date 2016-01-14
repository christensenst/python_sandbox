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

def return_example(f):
    def new_f():
        print "Entering", f.__name__
        result = f()
        print "Exited", f.__name__
        return result
    return new_f

@decorator_example
def test_function1():
    print "Inside test_function1"
    
@decorator_example
def test_function2():
    print "Inside test_function2"

@return_example
def no_return_something():
    print "doesn't return anything"

@return_example
def does_return_something():
    print "this thing returns something"
    return "the cool string"
    
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
    no_return_something()
    result = does_return_something()
    print "printing result: " + result
    print test_function1.__name__
