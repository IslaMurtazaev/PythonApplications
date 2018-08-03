# # Class definition
# class Animal(object):
#   """Makes cute animals."""
#   # For initializing our instance objects
#   def __init__(self, name, age, is_hungry):
#     self.name = name
#     self.age = age
#     self.is_hungry = is_hungry


# # Note that self is only used in the __init__()
# # function definition; we don't need to pass it
# # to our instance objects.

# zebra = Animal("Jeffrey", 2, True)
# giraffe = Animal("Bruce", 1, False)
# panda = Animal("Chad", 7, True)

# print(zebra.name, zebra.age, zebra.is_hungry)
# print(giraffe.name, giraffe.age, giraffe.is_hungry)
# print(panda.name, panda.age, panda.is_hungry)


# class Animal(object):
#   """Makes cute animals."""
#   is_alive = True
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def description(self):
#     print(self.name)
#     print(self.age)

# hippo = Animal('Hippo',3)
# print(hippo.is_alive)
# hippo.description()

# class ShoppingCart(object):
#   """Creates shopping cart objects
#   for users of our fine website."""
#   items_in_cart = {}
#   def __init__(self, customer_name):
#     self.customer_name = customer_name

#   def add_item(self, product, price):
#     """Add product to the cart."""
#     if not product in self.items_in_cart:
#       self.items_in_cart[product] = price
#       print product + " added."
#     else:
#       print product + " is already in the cart."

#   def remove_item(self, product):
#     """Remove product from the cart."""
#     if product in self.items_in_cart:
#       del self.items_in_cart[product]
#       print product + " removed."
#     else:
#       print product + " is not in the cart."

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
print(w1.getY(X,Y))