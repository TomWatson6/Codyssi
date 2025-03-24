from collections import defaultdict

input = open("input.txt").read().strip()

def parse_input(input: str) -> list[list[str]]:
    lines = [x.strip() for x in input.split("\n")]
    lines = [tuple(map(int, line[1:-1].split(", "))) for line in lines]
    return lines

def man_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part1(input: str) -> int:
    coords = parse_input(input)

    low = min(man_dist([0, 0], coord) for coord in coords)
    high = max(man_dist([0, 0], coord) for coord in coords)

    return high - low

def part2(input: str) -> int:
    coords = parse_input(input)
    largest = int(1e10)
    c = (0, 0)

    for coord in coords:
        m = man_dist([0, 0], coord)

        if m < largest:
            c = coord
            largest = m

    cs = []
            
    for coord in coords:
        cs.append((man_dist(coord, c), coord[0], coord[1]))

    cs = sorted(cs)

    return cs[1][0]

def find(nodes):
    curr = (0, 0)
    seen = set()
    dist = 0

    while not all(n in seen for n in nodes):
        dists = [(man_dist(curr, n), n[0], n[1]) for n in nodes if n not in seen]
        dists = sorted(dists)
        dist += dists[0][0]
        seen.add((dists[0][1], dists[0][2]))
        curr = (dists[0][1], dists[0][2])

    return dist

def part3(input: str) -> int:
    coords = parse_input(input)
    dist = find(coords)

    return dist

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
    print("Part 3:", part3(input))















