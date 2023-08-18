from Project7 import hillClimb
import unittest

class TestHillClimb(unittest.TestCase):

    def returns_local_value(self):
        self.assertEqual(hillClimb([6,5,5,5,4,3,2], 5),6)


    if __name__ == "__main__":
        unittest.main()