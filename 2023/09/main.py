rows = [
    [int(x) for x in value.split()]
    for value in open("09/input.txt").read().strip().split("\n")
]


def next_line(row):
    return [row[i] - row[i - 1] for i in range(1, len(row))]


def process(row):
    part1, part2, multiplier = 0, row[0], 1
    while any(row):
        part1 += row[-1]
        row = next_line(row)
        multiplier = -multiplier
        part2 += row[0] * multiplier

    return part1, part2


part1, part2 = map(sum, zip(*[process(row) for row in rows]))

print(part1, part2)
