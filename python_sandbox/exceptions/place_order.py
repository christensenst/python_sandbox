from order_exceptions import BaseOrderException
from orders import Order

class PlaceOrder(object):

    def __init__(self, name):
        self.name = name

    def place_order(self):
        try:
            order = Order("sweet tv", 7)
            order.complete(correct=False)
        except BaseOrderException as e:
            print e.message
            print e.friendly_message

if __name__ == '__main__':
    place_order = PlaceOrder("First")
    place_order.place_order()
