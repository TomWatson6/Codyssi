import unittest
import solution

input = open("simple_input.txt").read().strip()

class Day06Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(59, solution.part1(input))

    def test_part2(self):
        self.assertEqual(1742, solution.part2(input))

    def test_part3(self):
        self.assertEqual(2708, solution.part3(input))

if __name__ == "__main__":
    unittest.main()

















