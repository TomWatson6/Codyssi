from collections import defaultdict

input = open("input.txt").read().strip()

def parse_input(input: str) -> list[list[str]]:
    return [x.strip() for x in input.split("\n")]

def part1(input: str) -> int:
    lines = parse_input(input)
    total = 0

    for line in lines:
        for c in line:
            total += ord(c) - 64

    return total

def part2(input: str) -> int:
    lines = parse_input(input)
    total = 0

    for line in lines:
        num_chars = len(line) // 10
        chars = line[:num_chars] + line[-num_chars:]

        for c in chars:
            total += ord(c) - 64

        t = len(line) - (num_chars * 2)
        total += sum(int(x) for x in str(t))

    return total

def part3(input: str) -> int:
    lines = parse_input(input)
    total = 0

    for line in lines:
        parts = []
        i = 0
        last = line[i]
        count = 0

        while i < len(line):
            if line[i] == last:
                count += 1
            else:
                parts.append((last, count))
                count = 1
                last = line[i]

            i += 1

        parts.append((last, count))

        for char, count in parts:
            total += ord(char) - 64 + sum(int(x) for x in str(count))

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
    print("Part 3:", part3(input))















