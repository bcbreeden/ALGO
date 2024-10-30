import unittest
from leetcode.two_sum import two_sum

class TestAlgo(unittest.TestCase):
    def test_two_sum(self):
        result = two_sum([2,7,11,15], 9)
        self.assertListEqual(result, [0,1])

        result = two_sum([3,2,4], 6)
        self.assertListEqual(result, [1,2])

        result = two_sum([3,3], 6)
        self.assertListEqual(result, [0,1])

if __name__ == '__main__':
    unittest.main()
