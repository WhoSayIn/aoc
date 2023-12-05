class Solution:
    def __init__(self):
        self.grid = []

        with open("03/input.txt") as file:
            for line in file:
                self.grid.append(line.strip())

        self.width = len(self.grid[0])
        self.heigth = len(self.grid)

    def solve(self):
        parts = []

        for row in range(self.heigth):
            built_number = ""
            column_start = None

            for column in range(self.width):
                char = self.grid[row][column]

                if char.isdigit():
                    if column_start is None:
                        column_start = column
                    built_number += str(char)

                if (not char.isdigit() or column == self.width - 1) and len(
                    built_number
                ):
                    if self._has_symbol_in_border(row, column_start, len(built_number)):
                        parts.append(int(built_number))
                    built_number = ""
                    column_start = None

        return sum(parts)

    def _has_symbol_in_border(self, row, column, width):
        # top & bottom border
        for i in range(max(0, column - 1), min(self.width, column + width + 1)):
            if (row > 0 and self._is_symbol(self.grid[row - 1][i])) or (
                row < self.heigth - 1 and self._is_symbol(self.grid[row + 1][i])
            ):
                return True

        # left & right
        if (column > 0 and self._is_symbol(self.grid[row][column - 1])) or (
            column + width < self.width
            and self._is_symbol(self.grid[row][column + width])
        ):
            return True

        return False

    def _is_symbol(self, c):
        return c not in ".0123456789"


if __name__ == "__main__":
    s = Solution()
    print(s.solve())
