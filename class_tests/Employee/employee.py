

class Employee():
    """Employee information"""

    def __init__(self,first_name,last_name,annual_salary):
        self.first_name=first_name
        self.last_name=last_name
        self.annual_salary=annual_salary

    
    def give_default_raise(self,annual_raise=''):
        """Automatically gives an annual raise"""
        if not annual_raise:
            self.annual_salary+=5000
        elif annual_raise:
            self.annual_salary=self.annual_salary +int(annual_raise)+5000
        return self.annual_salary


    