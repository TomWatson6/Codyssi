import unittest
import solution

input = open("simple_input.txt").read().strip()

class Day02Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(9130674516975, solution.part1(input))

    def test_part2(self):
        self.assertEqual(1000986169836015, solution.part2(input))

    def test_part3(self):
        self.assertEqual(5496, solution.part3(input))

if __name__ == "__main__":
    unittest.main()

















