class Solution:
    def solve(self):
        with open("01/input.txt") as file:
            part1 = 0
            part2 = 0

            for line in file:
                part1 += self._first_and_last_digit(line)
                part2 += self._first_and_last_number(line)

            return (part1, part2)

    def _first_and_last_digit(self, line: str):
        for c in line:
            if c.isdigit():
                first_digit = c
                break

        for c in line[::-1]:
            if c.isdigit():
                last_digit = c
                break

        return int(first_digit + last_digit)

    def _first_and_last_number(self, line: str):
        numbers_map = {
            "one": "o1e",
            "two": "t2o",
            "three": "t3e",
            "four": "f4",
            "five": "f5e",
            "six": "6",
            "seven": "7n",
            "eight": "e8t",
            "nine": "n9e",
        }

        for key, value in numbers_map.items():
            line = line.replace(key, value)

        return self._first_and_last_digit(line)


if __name__ == "__main__":
    s = Solution()
    print(s.solve())
