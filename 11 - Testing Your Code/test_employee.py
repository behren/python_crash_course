import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class"""
    
    def setUp(self):
        """Creating Steve Rogers for use in Tests"""
        firstname = 'Steve'
        lastname = 'Rogers'
        salary = 420000.42
        self.steve = Employee(firstname, lastname, salary)
        
    def test_give_default_raise(self):
        """Try giving the employee a default raise"""
        self.steve.give_raise()
        self.assertEqual(self.steve.describe_employee(), 'Rogers, Steve - salary: $425,000.42')
        
    def test_give_custom_raise(self):
        """Giving Steve an Avengers worthy custom raise"""
        self.steve.give_raise(4200000000000.00)
        self.assertEqual(self.steve.describe_employee(), 'Rogers, Steve - salary: $4,200,000,420,000.42')
        
if __name__== '__main__':
    unittest.main()
