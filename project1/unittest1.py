import unittest
from addNumbers import addNumbers

class TestAddition(unittest.TestCase):
    def PositiveNumbers(self):
        answer = addNumbers(2, 3)
        self.assertEqual(answer, 5)

if __name__ == '__main__':
    unittest.main()
