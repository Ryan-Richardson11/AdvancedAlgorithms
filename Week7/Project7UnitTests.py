from Project7 import hillClimb
import unittest

class TestHillClimb(unittest.TestCase):

    def test_returns_local_value(self):
        arr = [6, 5, 5, 5, 4, 3, 2]
        expected_value = 6
        start_index = 5
        result_index = 0
        result = hillClimb(arr, start_index)
        self.assertEqual(result, (result_index,expected_value))

    def test_returns_local_value2(self):
        arr = [2, 5, 5, 5, 4, 3, 2]
        expected_value = 5
        start_index = 5
        result_index = 1
        result = hillClimb(arr, start_index)
        self.assertEqual(result, (result_index,expected_value))

if __name__ == "__main__":
    unittest.main()

# def hillClimb(arr, start_index):
#     if start_index == 0 or start_index == len(arr) - 1:
#         return arr[start_index]
#     elif arr[start_index] > arr[start_index-1] and arr[start_index] > arr[start_index+1]:
#         return arr[start_index]
#     elif arr[start_index] <= arr[start_index+1]:
#         return hillClimb(arr, start_index+1)
#     elif arr[start_index] <= arr[start_index-1]:
#         return hillClimb(arr, start_index-1)