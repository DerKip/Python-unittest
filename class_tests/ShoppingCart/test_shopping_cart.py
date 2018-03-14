import unittest
from shopping_cart import ShoppingCart,Shop

class ShoppinCartTestCase(unittest.TestCase):
   """Testing the ShoppingCart """
   def setUp(self):
        """
        Setting up the instance and assigning attributes for testing
        """
        self.my_cart=ShoppingCart()
        self.my_cart_2=Shop()

   def test_add_item_total(self):
       """Test if method adds items and updates total accordingly"""
       my_total=self.my_cart.add_item('Cookies',2,400)
       self.assertEqual(my_total,800)
   
#    def test_add_item_entry(self):
#        """Test if items dictionary is updated after adding an item"""
#        self.assertDictEqual(self.my_cart.items,{'Cookies':2},msg="Invalid dictionary")
   
   def test_remove_item_total(self):
       """Test whether total cash is updated after removing an item"""
       self.my_cart.add_item('Chocolate',5,300)
       self.my_cart.remove_item('Chocolate',2,300)
       self.assertEqual(self.my_cart.total,900,msg='Remove item method inaccurate')
        
   def test_remove_item_entry(self):
       """Tests whether items dictionary is updated after removing an item"""
       self.my_cart.add_item('Chocolate',5,300)
       self.my_cart.remove_item('Chocolate',2,300)
       self.assertDictEqual(self.my_cart.items,{'Chocolate':3},msg="Invalid dictionary")

   def test_exceeding_current_quantity(self):
       """Tests that all entries of an item are to be removed if quantity exeeds current."""
       self.my_cart.add_item('Chocolate',5,300) 
       self.my_cart.remove_item('Chocolate',7,300)
       self.assertDictEqual(self.my_cart.items,{},msg="Doesn't remove all entries if quantity exeeds the current")
    
   def test_checkout(self):
       """Tests balance after payment"""
       self.my_cart.add_item('Chocolate',2,300)
       self.assertEqual(self.my_cart.checkout(700),100) 

   def test_checkout_not_enough(self):
       """Tests if payment is enough """
       self.my_cart.add_item('Chocolate',2,300)
       self.assertEqual(self.my_cart.checkout(100),"Cash paid not enough") 
    
   def test_shop_if_subclass(self):
       """Tests whether Shop is a subclass of ShoppingCart"""
       self.assertTrue(issubclass(Shop,ShoppingCart) ,msg="Shop doesn't inherit from ShoppingCart")
    
   def test_shop_quantity(self):
       """Tests whether Shop quantity attribute is initialized to 100"""
       self.assertEqual(self.my_cart_2.quantity,100,msg="Shop quantity attribute not equal to 100")
    
   def test_override_remove_item(self):
       """Tests that calling Shop's remove_item with no arguments decrements quantity by one"""
       self.my_cart_2.add_item('Chocolate',5,300)
       self.my_cart_2.remove_item()
       self.assertDictEqual(self.my_cart_2.items,{'Chocolate':4},msg="Does not remove quantity by one")

#   def test_cart_property_initialization(self):
#     self.assertEqual(self.cart.total, 0, msg='Initial value of total not correct')
#     self.assertIsInstance(self.cart.items, dict, msg='Items is not a dictionary')

   def test_add_item(self):
       self.cart.add_item('Mango', 3, 10)
       self.assertEqual(self.cart.total, 30, msg='Cart total not correct after adding items')
       self.assertEqual(self.cart.items['Mango'], 3, msg='Quantity of items not correct after adding item')

#   def test_remove_item(self):
#     self.cart.add_item('Mango', 3, 10)
#     self.cart.remove_item('Mango', 2, 10)

#     self.assertEqual(self.cart.total, 10, msg='Cart total not correct after removing item')
#     self.assertEqual(self.cart.items['Mango'], 1, msg='Quantity of items not correct after removing item')



    

    
        

