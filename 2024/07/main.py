class Solution:
    def __init__(self, file_path="2024/07/input.txt"):
        with open(file_path) as file:
            self.input = file.readlines()

    def _can_calculate(self, target, numbers, current, cursor, incl_concat=False):
        if cursor >= len(numbers):
            return current == target

        next = numbers[cursor]

        return (
            self._can_calculate(
                target, numbers, current + next, cursor + 1, incl_concat
            )
            or self._can_calculate(
                target, numbers, current * next, cursor + 1, incl_concat
            )
            or (
                incl_concat
                and self._can_calculate(
                    target,
                    numbers,
                    int(f"{current}{next}"),
                    cursor + 1,
                    incl_concat,
                )
            )
        )

    def solve(self, incl_concat=False):
        result = 0
        for line in self.input:
            key_part, values_part = line.strip().split(":")
            key = int(key_part)
            values = [int(x) for x in values_part.split()]
            if self._can_calculate(key, values, values[0], 1, incl_concat):
                result += key
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.solve())
    print(s.solve(True))
