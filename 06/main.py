from math import prod

time_list, distance_list = [
    [int(value) for value in line.split()[1:]]
    for line in open("06/input.txt").read().strip().split("\n")
]

size = len(time_list)


def winning_combinations(time, distance_threshold):
    winning = 0
    for speed in range(time + 1):
        distance = (time - speed) * speed

        if distance > distance_threshold:
            winning += 1

    return winning


part1 = prod(
    [winning_combinations(time_list[i], distance_list[i]) for i in range(size)]
)
print(part1)

time = int("".join(str(value) for value in time_list))
distance = int("".join(str(value) for value in distance_list))
part2 = winning_combinations(time, distance)
print(part2)
