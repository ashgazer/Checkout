from Checkout import Checkout

def test_canAddItemPrice():
    checkout = Checkout()
    checkout.addItemPrice('a',1)