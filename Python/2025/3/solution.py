from collections import defaultdict

input = open("input.txt").read().strip()

def parse_input(input: str) -> list[list[str]]:
    lines = [x.strip().split() for x in input.split("\n")]
    return lines

def part1(input: str) -> int:
    lines = parse_input(input)

    total = 0

    for left, right in lines:
        left = [int(x) for x in left.split("-")]
        total += abs(left[1] - left[0]) + 1
        right = [int(x) for x in right.split("-")]
        total += abs(right[1] - right[0]) + 1

    return total

def part2(input: str) -> int:
    lines = parse_input(input)

    total = 0

    for left, right in lines:
        left = [int(x) for x in left.split("-")]
        right = [int(x) for x in right.split("-")]

        r = set(list(range(left[0], left[1] + 1)))
        r |= set(list(range(right[0], right[1] + 1)))
        total += len(r)

    return total

def part3(input: str) -> int:
    lines = parse_input(input)

    total = 0

    for (l1, r1), (l2, r2) in list(zip(lines, lines[1:])):
        l1 = [int(x) for x in l1.split("-")]
        r1 = [int(x) for x in r1.split("-")]
        l2 = [int(x) for x in l2.split("-")]
        r2 = [int(x) for x in r2.split("-")]

        r = set(list(range(l1[0], l1[1] + 1)))
        r |= set(list(range(r1[0], r1[1] + 1)))
        r |= set(list(range(l2[0], l2[1] + 1)))
        r |= set(list(range(r2[0], r2[1] + 1)))
        total = max(total, len(r))

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
    print("Part 3:", part3(input))















