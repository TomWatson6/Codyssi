import unittest
import solution

input = open("simple_input.txt").read().strip()

class Day04Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(1247, solution.part1(input))

    def test_part2(self):
        self.assertEqual(219, solution.part2(input))

    def test_part3(self):
        self.assertEqual(539, solution.part3(input))

if __name__ == "__main__":
    unittest.main()

















