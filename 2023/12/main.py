"""
Note: This is very unpolished! Part1 finishes under 0.15 seconds, but unfortunately
the solution did not scale for part2.
"""

data = [
    [item[0], list(map(int, item[1].split(",")))]
    for item in [
        line.strip().split() for line in open("12/input.txt").read().strip().split("\n")
    ]
]


def group_the_input(input):
    return [len(group) for group in input.split(".") if group]


def possible_combinations(input, condition):
    result = []

    def recurse(input, input_index=0):
        if input_index == len(input):
            if group_the_input(input) == condition:
                result.append(input)
        else:
            if input[input_index] == "?":
                next_possible_string = input[:input_index] + "#"
                next_possible_group = group_the_input(next_possible_string)

                can_add_hashtag = True
                for i in range(len(next_possible_group)):
                    if len(condition) > i and next_possible_group[i] > condition[i]:
                        can_add_hashtag = False
                        break

                if max(next_possible_group) > max(condition):
                    can_add_hashtag = False

                if len(next_possible_group) > len(condition):
                    can_add_hashtag = False

                if can_add_hashtag:
                    recurse(
                        input[:input_index] + "#" + input[input_index + 1 :],
                        input_index + 1,
                    )

                next_possible_string = input[:input_index] + "."
                next_possible_group = group_the_input(next_possible_string)
                can_add_dot = True

                if next_possible_group and max(next_possible_group) > max(condition):
                    can_add_dot = False

                if len(next_possible_group) <= len(condition):
                    for i in range(len(next_possible_group)):
                        if next_possible_group[i] != condition[i]:
                            can_add_dot = False
                            break
                else:
                    can_add_dot = False

                if (sum(condition) + len(condition)) - (
                    sum(next_possible_group) + len(next_possible_group)
                ) > len(input) - input_index:
                    can_add_dot = False

                if can_add_dot:
                    recurse(
                        input[:input_index] + "." + input[input_index + 1 :],
                        input_index + 1,
                    )

            else:
                recurse(input, input_index + 1)

    recurse(input)

    return result


result = 0
i = 0
for input, condition in data:
    # PART2
    # input = "?".join([input] * 5)
    # condition = condition * 5
    i += 1
    b = len(possible_combinations(input, condition))
    print(i, b)
    result += b

print(result)
