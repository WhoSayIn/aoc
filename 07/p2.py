from collections import Counter

hands = [line.split() for line in open("07/input.txt").read().strip().split("\n")]
card_types = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def get_hand_score(cards):
    j_quantity = cards.count("J")
    cards = cards.replace("J", "")
    counter = Counter(cards)
    if len(cards):
        most_frequent_card = counter.most_common(1)[0][0]
    else:  # the case of JJJJJ, return 5 of a kind
        return 25

    cards += most_frequent_card * j_quantity

    counter = Counter(cards)
    v = sorted(counter.values())
    return sum(value**2 for value in v[-2:])


hands_bids = []
for cards, bid in hands:
    hand_type = get_hand_score(cards)
    hands_bids.append([cards, hand_type, bid])

    hands_bids.sort(
        key=lambda x: (-x[1], [card_types.index(c) for c in x[0]]), reverse=True
    )

print(sum((i + 1) * int(r[2]) for i, r in enumerate(hands_bids)))
