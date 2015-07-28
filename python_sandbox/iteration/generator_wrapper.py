class GeneratorWrapper(object):
    """ Example of how to wrap an iterable object with a generator.
    """
    def __init__(self, container):
        self.container = container

    def iterator(self):
        for x in self.container:
            # do some validation to filter out invalid items
            if not ord(x) % 2:
                yield x


if __name__ == '__main__':
    thing = GeneratorWrapper(['a', 'b', 'c', 'd', 'e', 'f'])
    for x in thing.iterator():
        print x