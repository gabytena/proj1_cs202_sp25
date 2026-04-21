import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    def setUp(self):
        self.rect = GlobeRect(lo_lat=10.0, hi_lat=20.0, west_long=30.0, east_long=40.0)
        self.region = Region(rect=self.rect, name="Testland", terrain="other")
        self.rc = RegionCondition(region=self.region, year=2025, pop=1000, ghg_rate=5000.0)


    def test_holder(self):
        pass

    def test_3_1(self):
        self.assertEqual(emissions_per_capita(self.rc), 5)
    
    def test_3_2(self):
        self.assertAlmostEqual(area(self.rect), )



if __name__ == '__main__':
    unittest.main()
