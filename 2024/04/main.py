class Solution:
    def __init__(self, file_path="2024/04/input.txt"):
        with open(file_path) as f:
            self.grid = [list(row) for row in f.read().strip().split("\n")]
        self.size = len(self.grid)

    def is_within_bounds(self, r, c):
        return 0 <= r < self.size and 0 <= c < self.size

    def part1(self):
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        target = "MAS"

        def count_xmas_from(r, c):
            total = 0
            for dr, dc in directions:
                rr, cc, cursor = r + dr, c + dc, 0
                while (
                    self.is_within_bounds(rr, cc)
                    and self.grid[rr][cc] == target[cursor]
                ):
                    cursor += 1
                    if cursor == len(target):
                        total += 1
                        break
                    rr += dr
                    cc += dc
            return total

        return sum(
            count_xmas_from(r, c)
            for r in range(self.size)
            for c in range(self.size)
            if self.grid[r][c] == "X"
        )

    def part2(self):
        diagonal_offsets = [
            [(-1, -1), (1, 1)],
            [(-1, 1), (1, -1)],
        ]
        target_set = {"M", "S"}

        def is_valid_mas(r, c):
            for offsets in diagonal_offsets:
                try:
                    symbols = {self.grid[r + dr][c + dc] for dr, dc in offsets}
                    if symbols != target_set:
                        return False
                except IndexError:
                    return False
            return True

        return sum(
            is_valid_mas(r, c)
            for r in range(self.size)
            for c in range(self.size)
            if self.grid[r][c] == "A"
        )


if __name__ == "__main__":
    s = Solution()
    print(s.part1())
    print(s.part2())
