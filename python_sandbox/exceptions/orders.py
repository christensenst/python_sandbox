from order_exceptions import OrderCompleteException

class Order(object):

    def __init__(self, product, number_of_items):
        self.product = product
        self.number_of_items = number_of_items

    def complete(self, correct=True):
        if correct:
            print "Your order is complete"
        else:
            raise OrderCompleteException("Bob", "this is the message", self.number_of_items)
