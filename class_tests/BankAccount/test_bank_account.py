
import unittest
from bank_account import BankAccount

class BankAccountTestCase(unittest.TestCase):

    def setUp(self):
        self.my_account=BankAccount()
    
    def test_deposit(self):
        self.my_account.deposit(3000)
        self.assertEqual(self.my_account.balance,5000,msg="Inacurate method")
    
    def test_withdraw(self):
        self.my_account.withdraw(1000)
        self.assertEqual(self.my_account.balance,1000,msg="Invalid method")
    
    def test_invalid_transaction(self):
        self.assertEqual(self.my_account.withdraw(2500),"invalid transaction!",msg='invalid transaction not handled')
 