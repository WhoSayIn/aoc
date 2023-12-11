grid = [
    [column for column in row]
    for row in open("11/input.txt").read().strip().split("\n")
]

width = len(grid[0])
height = len(grid)

empty_rows = []
for i in range(height):
    if all(cell == "." for cell in grid[i]):
        empty_rows.append(i)

empty_columns = []
for i in range(width):
    if all(cell == "." for cell in (row[i] for row in grid)):
        empty_columns.append(i)

stars = []
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == "#":
            stars.append((r, c))


def distance_with_expansion(s1, s2, expansion):
    empty_rows_in_between = len(
        [row for row in empty_rows if s1[0] > row > s2[0] or s2[0] > row > s1[0]]
    )

    empty_columns_in_between = len(
        [
            column
            for column in empty_columns
            if s1[1] > column > s2[1] or s2[1] > column > s1[1]
        ]
    )

    return (
        abs(s1[0] - s2[0])
        + abs(s1[1] - s2[1])
        + empty_rows_in_between * expansion
        + empty_columns_in_between * expansion
    )


part1 = part2 = 0
for i in range(len(stars)):
    for j in range(i + 1, len(stars)):
        part1 += distance_with_expansion(stars[i], stars[j], 1)
        part2 += distance_with_expansion(stars[i], stars[j], 999999)

print(part1, part2)
