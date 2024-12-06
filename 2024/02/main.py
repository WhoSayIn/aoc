class Solution:
    def is_safe(self, line):
        min_diff, max_diff = 1, 3
        direction = None

        for i in range(len(line) - 1):
            diff = line[i] - line[i + 1]
            new_direction = diff > 0

            if (
                direction is not None
                and new_direction != direction
                or not (min_diff <= abs(diff) <= max_diff)
            ):
                return False

            direction = new_direction

        return True

    def is_safe_dampened(self, line):
        if self.is_safe(line):
            return True

        return any(self.is_safe(line[:i] + line[i + 1 :]) for i in range(len(line)))

    def read_lines(self, file_path):
        with open(file_path) as file:
            return [list(map(int, line.strip().split())) for line in file]

    def part1(self):
        lines = self.read_lines("2024/02/input.txt")
        return sum(self.is_safe(line) for line in lines)

    def part2(self):
        lines = self.read_lines("2024/02/input.txt")
        return sum(self.is_safe_dampened(line) for line in lines)


if __name__ == "__main__":
    s = Solution()
    print(s.part1())
    print(s.part2())
