import unittest
from removeElement import Solution


class TestSum(unittest.TestCase):

    def test_remove(self):
        s = Solution()
        b = [3, 2, 2, 3]
        n = 2
        val = 3
        s.removeElement(b, val)
        self.assertEqual(b[:n], [2, 2], "Should be [2,2]")

    def test_longer_remove(self):
        s = Solution()
        b = [0, 1, 2, 2, 3, 0, 4, 2]
        n = 5
        val = 2
        s.removeElement(b, val)
        self.assertEqual(sorted(b), sorted([0,1,4,0,3]), "Should be [0,1,4,0,3]")

    def test_empty(self):
        s = Solution()
        b = []
        n = 0
        val = 3
        s.removeElement(b, val)
        self.assertEqual(b, [], "Should be []")

    def test_singular(self):
        s = Solution()
        b = [1]
        n = 0
        val = 1
        s.removeElement(b, val)
        self.assertEqual(b, [], "Should be []")

    def test_double(self):
        s = Solution()
        b = [1,2]
        n = 0
        val = 2
        s.removeElement(b, val)
        self.assertEqual(b, [1], "Should be [1]")


if __name__ == '__main__':
    unittest.main()
