import unittest
from TimeCompare import TimeCompare

class Test_TimeCompare(unittest.TestCase):
    timeCompare = TimeCompare()

    def test_convertTo24Hours(self):
        self.assertEqual(self.timeCompare.convertTo24Hours("", ""), "")

if __name__ == '__main__':
    unittest.main()