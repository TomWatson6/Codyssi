import unittest
import solution

input = open("simple_input.txt").read().strip()

class Day03Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(43, solution.part1(input))

    def test_part2(self):
        self.assertEqual(35, solution.part2(input))

    def test_part3(self):
        self.assertEqual(9, solution.part3(input))

if __name__ == "__main__":
    unittest.main()

















