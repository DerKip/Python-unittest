# class ShoppingCart():

#     def __init__(self):
#         self.total = 0
#         self.items = dict()

#     def add_item(self, item_name, quantity, price):
#         if item_name != None and quantity >= 1:
#             self.items.update({item_name: quantity})
#         if quantity and price >= 1:
#             self.total += (quantity * price)
#         return self.total

#     def remove_item(self, item_name, quantity, price):
#         self.total -= (quantity * price)
#         try:
#             if quantity >= self.items[item_name]:
#                 self.items.pop(item_name, None)
#             self.items[item_name] -= quantity
#         except(KeyError, RuntimeError):
#             pass

#     def checkout(self, cash_paid):
#         balance = 0
#         if cash_paid < self.total:
#             return "Cash paid not enough"
#         balance = cash_paid - self.total
#         return balance


# class Shop(ShoppingCart):

#     def __init__(self):
#         self.quantity = 100

#     def remove_item(self):
#         self.quantity -= 1

class ShoppingCart():
  def __init__(self):
    self.total = 0
    self.items = {}

  def add_item(self, item_name, quantity, price):
    self.total += price*quantity
    self.items.update({item_name: quantity})

  def remove_item(self, item_name, quantity, price):
    if item_name in self.items:
      if quantity < self.items[item_name] and quantity > 0:
        self.items[item_name] -= quantity
        self.total -= price*quantity
      
      elif quantity >= self.items[item_name]:
        self.total -= price*self.items[item_name]
        del self.items[item_name]


  def checkout (self, cash_paid):
    if cash_paid >= self.total:
      return cash_paid - self.total
    return "Cash paid not enough"

class Shop(ShoppingCart):
  
  def __init__(self):
    self.quantity = 100

  def remove_item(self):
    self.quantity -=1
