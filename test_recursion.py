import unittest
from recursion import fibonacci, gcd, compareTo

class TestRecursionFunctions(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 0)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(11), 55)
       

    def test_gcd(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(12, 15), 3)
        

    def test_compareTo(self):
        self.assertEqual(compareTo("", ""), 0)
        self.assertEqual(compareTo("abc", "abc"), 0)
        self.assertEqual(compareTo("abc", "abd"), -1) # Assuming compareTo returns -1, 0, 1
        
if __name__ == '__main__':
    unittest.main()
