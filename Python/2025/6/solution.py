from collections import defaultdict

input = open("input.txt").read().strip()

def parse_input(input: str) -> list[list[str]]:
    return input.strip()

def value(c):
    if c.isupper():
        return ord(c) - 64 + 26
    elif c.islower():
        return ord(c) - 96
    else:
        return 0

def find(chars):
    total = 0
    last = 0

    for i in range(len(chars)):
        curr = chars[i]
        if not curr.isalpha():
            curr = last * 2 - 5
            curr = (curr - 1) % 52 + 1
            last = curr
            total += curr
        else:
            total += value(curr)
            last = value(curr)

    return total

def part1(input: str) -> int:
    chars = parse_input(input)

    return sum(c.isalpha() for c in chars)

def part2(input: str) -> int:
    chars = parse_input(input)

    return sum(value(c) for c in chars)

def part3(input: str) -> int:
    chars = parse_input(input)

    return find(chars)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
    print("Part 3:", part3(input))















