class IterationWrapper(object):
    """ Example of how to make a custom iterable object.  The iterable object is also it's own iterator
    """
    def __init__(self, container):
        self.container = container

    def __iter__(self):
        return iter(self.container)


if __name__ == '__main__':
    thing = IterationWrapper(['a', 'b', 'c', 'd'])
    for x in thing:
        print x