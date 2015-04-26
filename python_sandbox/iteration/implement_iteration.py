class CustomList(object):
    """ Example of how to make a custom iterable object.  The iterable object is also it's own iterator
    """
    def __init__(self, container):
        self.container = container
        self.current = 0

    def __iter__(self):
        return self

    def next(self):
        if self.current >= len(self.container):
            raise StopIteration
        else:
            x = self.container[self.current]
            self.current += 1
            return x


if __name__ == '__main__':
    thing = CustomList(['a', 'b', 'c', 'd'])
    for x in thing:
        print x
