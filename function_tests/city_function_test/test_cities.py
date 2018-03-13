import unittest
from city_functions import *

class TestCityFunctions(unittest.TestCase):
    
    def test_city_country(self):
        result=city_country('cairo','egypt')
        self.assertEqual(result,'Cairo, Egypt')
    
    def test_city_country_population(self):
        result=city_country('kampala','uganda',200000)
        self.assertEqual(result,'Kampala, Uganda - population 200000')




# unittest.main()

