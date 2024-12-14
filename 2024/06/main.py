class Solution:
    def __init__(self, file_path="2024/06/input.txt"):
        with open(file_path) as f:
            self.grid = [list(line.strip()) for line in f if line.strip()]
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.part1_visited = set()

    def _starting_point(self):
        for r, row in enumerate(self.grid):
            for c, val in enumerate(row):
                if val == "^":
                    return r, c

    def _next_direction(self, direction):
        return self.directions[(self.directions.index(direction) + 1) % 4]

    def _is_outside_grid(self, row, column):
        return (
            row < 0
            or row >= len(self.grid)
            or column < 0
            or column >= len(self.grid[row])
        )

    def _is_obstacle(self, row, column):
        return self.grid[row][column] in ["#", "X"]

    def _next_position(self, row, column, direction):
        next_row, next_column = (
            row + direction[0],
            column + direction[1],
        )

        if not self._is_outside_grid(next_row, next_column) and self._is_obstacle(
            next_row, next_column
        ):
            return self._next_position(row, column, self._next_direction(direction))

        return next_row, next_column, direction

    def part1(self):
        visited = set()
        direction = (-1, 0)
        row, column = self._starting_point()

        while True:
            if (row, column) not in visited:
                visited.add((row, column))

            row, column, direction = self._next_position(row, column, direction)

            if self._is_outside_grid(row, column):
                break

        self.part1_visited = visited

        return len(visited)

    def part2(self):
        result = 0

        for r, c in self.part1_visited:
            if self.grid[r][c] == ".":
                self.grid[r][c] = "X"

                visited = set()
                direction = (-1, 0)
                row, column = self._starting_point()

                while True:
                    if (row, column, direction) not in visited:
                        visited.add((row, column, direction))
                    else:
                        result += 1
                        break

                    row, column, direction = self._next_position(row, column, direction)

                    if self._is_outside_grid(row, column):
                        break

                self.grid[r][c] = "."

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.part1())
    print(s.part2())
