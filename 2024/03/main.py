import re


class Solution:
    def __init__(self, file_path="2024/03/input.txt"):
        with open(file_path, "r") as f:
            self.input_data = f.read()

        self.pattern_part1 = re.compile(r"mul\((\d+),(\d+)\)")
        self.pattern_part2 = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")

    def part1(self):
        return sum(
            int(a) * int(b) for a, b in self.pattern_part1.findall(self.input_data)
        )

    def part2(self):
        enabled = True
        result = 0

        for match in self.pattern_part2.finditer(self.input_data):
            token = match.group(0)
            if token == "do()":
                enabled = True
            elif token == "don't()":
                enabled = False
            elif enabled:
                a, b = match.groups()
                result += int(a) * int(b)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.part1())
    print(s.part2())
