import unittest
from city_functions import *

class TestCityFunctions(unittest.TestCase):
    
    def test_city_country(self):
        result=city_country('cairo','egypt')
        self.assertEqual(result,'Cairo, Egypt')
    
    def test_city_country_population(self):
        result=city_country('nairobi','kenya',300000)
        self.assertEqual(result,'Nairobi, Kenya - population 300000')




# unittest.main()

