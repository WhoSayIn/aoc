from itertools import combinations


class Solution:
    def __init__(self, file_path="2024/05/input.txt"):
        with open(file_path) as file:
            rules_input, updates_input = file.read().strip().split("\n\n")
        self.rules = {tuple(map(int, line.split("|"))) for line in rules_input.split()}
        self.reversed_rules = {tuple(reversed(rule)) for rule in self.rules}
        self.updates = [
            list(map(int, line.split(","))) for line in updates_input.split()
        ]

    def _is_valid_update(self, update):
        return all(
            tuple(pair) not in self.reversed_rules for pair in combinations(update, 2)
        )

    def _fix_update(self, update):
        while True:
            for pair in combinations(update, 2):
                if tuple(pair) in self.reversed_rules:
                    i, j = update.index(pair[0]), update.index(pair[1])
                    update[i], update[j] = update[j], update[i]
                    break
            else:
                break
        return update

    def part1(self):
        return sum(
            update[len(update) // 2]
            for update in self.updates
            if self._is_valid_update(update)
        )

    def part2(self):
        return sum(
            self._fix_update(update)[len(update) // 2]
            for update in self.updates
            if not self._is_valid_update(update)
        )


if __name__ == "__main__":
    s = Solution()
    print(s.part1())
    print(s.part2())
