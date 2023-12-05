class Solution:
    def __init__(self):
        self.cards = list(open("04/input.txt"))

    def solve(self):
        result_p1 = 0
        multipliers = [1] * len(self.cards)

        for index, card in enumerate(self.cards):
            splitted_card = card.strip().split(":")

            numbers = splitted_card[1].split("|")
            winning_numbers = set([number.strip() for number in numbers[0].split()])
            cards_numbers = set([number.strip() for number in numbers[1].split()])
            matching_numbers = cards_numbers.intersection(winning_numbers)

            for m in range(multipliers[index]):
                for i in range(
                    index + 1,
                    min(index + len(matching_numbers) + 1, len(self.cards) - 1),
                ):
                    multipliers[i] += 1

            power = 2 ** (len(matching_numbers) - 1) if len(matching_numbers) > 0 else 0
            result_p1 += power

        return result_p1, sum(multipliers)


if __name__ == "__main__":
    s = Solution()
    print(s.solve())
