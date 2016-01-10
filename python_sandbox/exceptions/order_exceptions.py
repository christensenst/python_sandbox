class BaseOrderException(Exception):
    pass



class OrderCompleteException(BaseOrderException):
    
    def __init__(self, customer_name, message, number_of_items):
        self.message = message
        self.friendly_message = "Customer {} already purchased {} of these items.".format(
            customer_name,
            str(number_of_items)
        )
