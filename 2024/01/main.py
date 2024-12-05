from collections import Counter


class Solution:
    def part1(self):
        with open("2024/01/input.txt") as file:
            left, right = zip(*(map(int, line.split()) for line in file))

        left_sorted = sorted(left)
        right_sorted = sorted(right)

        return sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

    def part2(self):
        with open("2024/01/input.txt") as file:
            left, right = zip(*(map(int, line.split()) for line in file))

        right_counter = Counter(right)

        return sum(l * right_counter[l] for l in left)


if __name__ == "__main__":
    s = Solution()
    print(s.part1())
    print(s.part2())
