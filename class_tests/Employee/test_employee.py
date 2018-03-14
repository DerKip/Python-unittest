
import unittest
from employee import Employee,Shop


class EmployeeTestCase(unittest.TestCase):
    """Testing the Employee class"""

    def setUp(self):
        """
        Create Employee and assign values to properties
        """
        first_name="John"
        last_name="Doe"
        annual_salary=1000
        self.my_employee=Employee(first_name,last_name,annual_salary)
       
    def test_give_default_raise(self):
        "Tests if default raise is given"
        new_annual_salary=self.my_employee.give_default_raise()
        self.assertEqual(new_annual_salary,6000)
    
    def test_give_custom_raise(self):
        "Tests custom give_raise Employee method"
        new_annual_salary=self.my_employee.give_default_raise(1000)
        self.assertEqual(new_annual_salary,7000)
        

# unittest.main()