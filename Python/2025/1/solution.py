from collections import defaultdict

input = open("input.txt").read().strip()

def parse_input(input: str, p3: bool) -> list[list[str]]:
    lines = [x.strip() for x in input.split("\n")]
    if p3:
        start = int(lines[0] + lines[1])
        numbers = [int(x) for x in lines[2:-1]]
    else:
        start = int(lines[0])
        numbers = [int(x) for x in lines[1:-1]]

    signs = lines[-1]

    return start, numbers, signs

def part1(input: str) -> int:
    start, numbers, signs = parse_input(input, False)
    curr = start

    for i in range(len(numbers)):
        n = numbers[i]
        sign = signs[i]

        if sign == '+':
            curr += n
        else:
            curr -= n

    return curr

def part2(input: str) -> int:
    start, numbers, signs = parse_input(input, False)
    curr = start

    for i in range(len(numbers)):
        n = numbers[i]
        sign = signs[len(numbers) - i - 1]

        if sign == '+':
            curr += n
        else:
            curr -= n

    return curr

def part3(input: str) -> int:
    start, numbers, signs = parse_input(input, True)
    signs = signs[::-1]
    curr = start

    for i in range(0, len(numbers), 2):
        n = int(str(numbers[i]) + str(numbers[i + 1]))
        sign = signs[i // 2]

        if sign == '+':
            curr += n
        else:
            curr -= n

    return curr



if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
    print("Part 3:", part3(input))















