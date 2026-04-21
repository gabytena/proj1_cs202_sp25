import unittest
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    def setUp(self):
       pass


    def test_holder(self):
        pass

    def test_3_1_1(self):
         rc = region_conditions[0]
         expected = rc.ghg_rate/rc.pop
         self.assertAlmostEqual(emissions_per_capita(rc), expected, places = 5)
    
    def test_3_1_2(self):
         rc = region_conditions[1]
         expected = rc.ghg_rate/rc.pop
         self.assertAlmostEqual(emissions_per_capita(rc), expected, places = 5)
    
    def test_3_2(self):
       gr = region_conditions[2].region.rect
       self.assertGreater(area(gr), 0)

    def test_3_3(self):
        rc = region_conditions[3]
        expected = rc.ghg_rate/ area(rc.region.rect)
        self.assertAlmostEqual(emissions_per_square_km(rc), expected, places = 5)

    def test_3_4(self):
        self.assertIn(densest(region_conditions), ["London", "Sydney", "Polynesia", "Central Coast"])

    def test_4(self):
        rc = region_conditions[2]
        og = rc
        x = project_condition(rc, 4)
        self.assertEqual(rc, og)    



if __name__ == '__main__':
    unittest.main()
