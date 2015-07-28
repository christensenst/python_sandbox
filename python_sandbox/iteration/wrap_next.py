class WrapNext(object):
    """ Example of how to wrap an iterable object with a generator.
    """
    def __init__(self, container):
        self.container = container

    def __iter__(self):
        return self

    def next(self):
        if not hasattr(self, 'iterator'):
            self.iterator = iter(self.container)
        while True:
            # StopIteration should already be handled from the list iterator
            x = self.iterator.next()
            if not ord(x) % 2:
                return x



if __name__ == '__main__':
    thing = WrapNext(['a', 'b', 'c', 'd', 'e', 'f'])
    # should print b, d, f
    for x in thing:
        print x