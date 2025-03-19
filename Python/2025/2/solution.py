from collections import defaultdict

input = open("input.txt").read().strip()

def parse_input(input: str) -> list[list[str]]:
    functions, numbers = [x.strip() for x in input.split("\n\n")]
    functions = [int(x.strip().split()[-1]) for x in functions.split("\n")]
    add, mult, power = functions
    numbers = [int(x.strip()) for x in numbers.split("\n")]

    return add, mult, power, numbers

def convert(num, add, mult, power):
    return num ** power * mult + add

def part1(input: str) -> int:
    add, mult, power, numbers = parse_input(input)

    median = sorted(numbers)[len(numbers) // 2]

    cost = convert(median, add, mult, power)

    return cost

def part2(input: str) -> int:
    add, mult, power, numbers = parse_input(input)

    even = sum(n for n in numbers if n % 2 == 0)

    cost = convert(even, add, mult, power)

    return cost

def part3(input: str) -> int:
    add, mult, power, numbers = parse_input(input)

    best = max(n for n in numbers if convert(n, add, mult, power) <= 15000000000000)

    return best

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
    print("Part 3:", part3(input))















