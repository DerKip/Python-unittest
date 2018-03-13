
import unittest
from name_function import *

class NameTestCase(unittest.TestCase):
#    '''tests for name_function.py'''

   def test_first_last_name(self):
       formated_name=get_formatted_name('marcus','mouya')
       self.assertEqual(formated_name,'Marcus Mouya')
   
   def test_email(self):
       result=get_email('marcus','mouya')
       self.assertEqual(result,'marcusmouya@company.com')
    

# unittest.main()

  

   
    

    
    