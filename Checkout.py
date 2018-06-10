
class Checkout:

    def __init__(self):
        self.total = 0
        self.prices = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        self.total += self.prices[item]

    def calculateTotal(self):
        return self.total