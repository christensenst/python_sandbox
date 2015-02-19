# The Iteration Protocol
# Any object with a next() method (Python 2.X) to advance to a next result, which raises StopIteration at the end of
# the series of results, is considered an iterator in Python.  Any such object may also be stepped through with a for
# loop or other iteration tool, because all iteration tools normally work internally by calling next() on each
# iteration and cathcing the StopIteration exception to determine when to exit.
#
# The iteration protocol is really based on two objects, used in two distinct steps by iteration tools:
#     the iterable object you request iteration for, whose __iter__ is run by iter
#     the iterator object returned by the iterable that actually produces values during the iteration, whose next
#         method is run by the built-in next() and raises StopIteration when finished producing results.
# In some cases, such as files, these two objects are the same

def basic_iteration():
    # files have a method called readline.  At the end of the file, an empty string is returned.
    f = open('__init__.py')
    print f.readline()
    print f.readline()
    print f.readline()
    print f.readline()
    print f.readline()
    f.close()

    # files also have a method called next.  The only noticeable difference is that next() raises a builtin
    # StopIteration exception at end of file instead of returning an empty string.
    f = open('__init__.py')
    try:
        print f.next()
        print f.next()
        print f.next()
        print f.next()
        print f.next()
    except StopIteration:
        print "Whoa, we really had to catch StopIteration, otherwise this would've blown sky high!"
    finally:
        f.close()

    # the best way to read a text file line by line is to not read it at all - instead, allow the for loop to
    # automatically call next() to advance to the next line on each iteration.  When the for loop begins, it first
    # obtains an iterator from the iterable object by passing it to the iter built-in function; the object returned
    # by iter in turn has the required next method.  The iter function internally runs the __iter__ method.
    for line in open('__init__.py'):
        print line

    #FYI: iterators run at C language speed inside Python

    # we can also manually iterate by calling the built-in next() method and passing in an iterator object
    f = open('__init__.py')
    try:
        print next(f)
        print next(f)
        print next(f)
        print next(f)
        print next(f)
    except StopIteration:
        print "yep, had to catch StopIteration again"

    # Here's how it works for sequence objects (which are not their own iterator object)
    numbers = [1, 2, 3]
    iterator = iter(numbers)
    print iterator.next()
    print iterator.next()
    print iterator.next()


if __name__ == '__main__':
    basic_iteration()