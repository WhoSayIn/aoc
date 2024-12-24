class Solution:
    def __init__(self, file_path="2024/10/input.txt"):
        with open(file_path) as f:
            self.grid = [
                [int(c.replace(".", "-1")) for c in line.strip()]
                for line in f
                if line.strip()
            ]

    def _starting_points(self):
        starting_points = []
        for r, row in enumerate(self.grid):
            for c, char in enumerate(row):
                if char == 0:
                    starting_points.append((r, c))
        return starting_points

    def _bound_check(self, r, c):
        return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0])

    def part1(self):
        starting_points = self._starting_points()
        score = 0

        for starting_point in starting_points:
            visited = set()
            found_9s = set()
            stack = [starting_point]

            while stack:
                i, j = stack.pop()
                if (i, j) in visited:
                    continue
                visited.add((i, j))

                if self.grid[i][j] == 9:
                    found_9s.add((i, j))

                for x, y in [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1),
                ]:
                    if (
                        self._bound_check(x, y)
                        and self.grid[x][y] != -1
                        and self.grid[x][y] == self.grid[i][j] + 1
                    ):
                        stack.append((x, y))
            score += len(found_9s)

        return score

    def part2(self):
        starting_points = self._starting_points()
        score = 0

        for starting_point in starting_points:
            found_9s = []
            stack = [starting_point]

            while stack:
                i, j = stack.pop()

                if self.grid[i][j] == 9:
                    found_9s.append((i, j))

                for x, y in [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1),
                ]:
                    if (
                        self._bound_check(x, y)
                        and self.grid[x][y] != -1
                        and self.grid[x][y] == self.grid[i][j] + 1
                    ):
                        stack.append((x, y))
            score += len(found_9s)

        return score


if __name__ == "__main__":
    s = Solution()
    print(s.part1())
    print(s.part2())
