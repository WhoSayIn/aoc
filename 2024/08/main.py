from collections import defaultdict
from itertools import permutations


class Solution:
    def __init__(self, file_path="2024/08/input.txt"):
        with open(file_path) as f:
            self.grid = [list(line.strip()) for line in f if line.strip()]
        self.size = len(self.grid)
        self.antennas = defaultdict(list)
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell != ".":
                    self.antennas[cell].append((r, c))

    def _mirror(self, p1, p2, multiplier=1):
        p = (multiplier * (p2[0] - p1[0]) + p2[0], multiplier * (p2[1] - p1[1]) + p2[1])

        if not (0 <= p[0] < self.size and 0 <= p[1] < self.size):
            return None
        return p

    def part1(self):
        antinodes = set()
        for antenna, points in self.antennas.items():
            for p1, p2 in permutations(points, 2):
                p3 = self._mirror(p1, p2)
                if p3 is not None:
                    antinodes.add(p3)
        return len(antinodes)

    def part2(self):
        antinodes = set()
        for antenna, points in self.antennas.items():
            for p1, p2 in permutations(points, 2):
                for i in range(self.size):
                    p3 = self._mirror(p1, p2, i)
                    if p3 is not None:
                        antinodes.add(p3)
        return len(antinodes)


if __name__ == "__main__":
    s = Solution()
    print(s.part1())
    print(s.part2())
