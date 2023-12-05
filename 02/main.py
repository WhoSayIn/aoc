from math import prod


class Solution:
    def __init__(self, red, green, blue):
        self.conditions = {
            "red": red,
            "green": green,
            "blue": blue,
        }

    def solve(self):
        with open("02/input.txt") as file:
            part1 = 0
            part2 = 0

            for line in file:
                part1 += self._part_1(line)
                part2 += self._part_2(line)

            return (part1, part2)

    def _part_1(self, line: str):
        state = {
            "red": True,
            "green": True,
            "blue": True,
        }

        splitted_line = line.rstrip().split(":")

        game_id = int(splitted_line[0].split()[1])
        picks = splitted_line[1].split(";")

        for pick in picks:
            cubes = pick.strip().split(",")
            for cube in cubes:
                splitted_cube = cube.split()
                amount = int(splitted_cube[0])
                color = splitted_cube[1]

                if amount > self.conditions[color]:
                    state[color] = False

        if all(value for value in state.values()):
            return game_id

        return 0

    def _part_2(self, line: str):
        state = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        splitted_line = line.rstrip().split(":")

        picks = splitted_line[1].split(";")

        for pick in picks:
            cubes = pick.strip().split(",")
            for cube in cubes:
                splitted_cube = cube.split()
                amount = int(splitted_cube[0])
                color = splitted_cube[1]

                if amount > state[color]:
                    state[color] = amount

        return prod(state.values())


if __name__ == "__main__":
    s = Solution(12, 13, 14)
    print(s.solve())
