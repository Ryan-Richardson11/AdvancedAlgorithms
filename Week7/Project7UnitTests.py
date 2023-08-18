from Project7 import hillClimb
import unittest

class TestHillClimb(unittest.TestCase):

    def test_returns_local_value(self):
        arr = [6, 5, 5, 5, 4, 3, 2]
        expected_value = 6
        start_index = 5
        result = hillClimb(arr, start_index)
        self.assertEqual(result, expected_value)

    def test_returns_local_value2(self):
        arr = [2, 5, 5, 5, 4, 3, 2]
        expected_value = 5
        start_index = 5
        result = hillClimb(arr, start_index)
        self.assertEqual(result, expected_value)

if __name__ == "__main__":
    unittest.main()