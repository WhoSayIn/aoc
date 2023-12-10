from operator import add

grid = [
    [column for column in row]
    for row in open("10/input.txt").read().strip().split("\n")
]

# encapsulate the grid with dots, so no need to care about edges. cc @elhu
grid = (
    [["."] * (len(grid[0]) + 2)]
    + [["."] + row + ["."] for row in grid]
    + [["."] * (len(grid[0]) + 2)]
)


for row in grid:
    if "S" in row:
        start = (grid.index(row), row.index("S"))
        break


NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)

# map of pipes and possible directions you can go from that pipe
pipes = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
    ".": [],
    "S": [NORTH, SOUTH, EAST, WEST],
}


def symbol_at(coordinate):
    return grid[coordinate[0]][coordinate[1]]


def move(source, direction):
    return tuple(map(add, source, direction))


def dfs(coordinate):
    stack = [coordinate]
    visited = {coordinate}

    while stack:
        current = stack.pop()
        current_symbol = symbol_at(current)
        for direction in pipes[current_symbol]:
            neighbor = move(current, direction)
            # dot check only for the starting point
            if neighbor not in visited and symbol_at(neighbor) != ".":
                stack.append(neighbor)
                visited.add(neighbor)

    return len(visited) // 2


part1 = dfs(start)
print(part1)
