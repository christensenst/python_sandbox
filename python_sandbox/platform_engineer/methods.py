# Static methods and explicit class names may be a better solution for processing data local to a class
# Class methods may be better suited to processing data that may differ for each class in a hierarchy

class Spam(object):
    num_instances = 0
    def __init__(self):
        Spam.num_instances += 1
    @staticmethod
    def print_num_instances():
        print "Number of instances: " + str(Spam.num_instances)

class Sub(Spam):
	@staticmethod
	def print_num_instances():
		print "inside Sub"
		Spam.print_num_instances()

class Bug(object):
    num_instances = 0
    def __init__(self):
	    Bug.num_instances += 1
    @classmethod
    def print_num_instances(cls):
        print "Number of instances: " + str(cls.num_instances)
        print cls

class Spider(Bug):
    @classmethod
    def print_num_instances(cls):
        print "Inside Spider"
        print "Number of instances: " + str(cls.num_instances)

class First(object):
    num_instances = 0
    @classmethod
    def count(cls):
        cls.num_instances += 1
    def __init__(self):
        self.count()

class Second(First):
    num_instances = 0
    def __init__(self):
        First.__init__(self)

class Third(First):
    num_instances = 0
    
if __name__ == '__main__':
    x = First()
    y1, y2 = Second(), Second()
    z1, z2, z3 = Third(), Third(), Third()
    print x.num_instances, y1.num_instances, z1.num_instances  # 1, 2, 3
    print First.num_instances, Second.num_instances, Third.num_instances # 1, 2, 3
