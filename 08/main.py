from math import lcm

directions, routes = open("08/input.txt").read().strip().split("\n\n")

routes_map = {
    location: targets.strip(")").split(", ")
    for location, targets in [route.split(" = (") for route in routes.split("\n")]
}


# PART1
def step_count(source, target):
    counter, directions_len = 0, len(directions)
    while source != target:
        source = routes_map[source][directions[counter % directions_len] == "R"]
        counter += 1
    return counter


part1 = step_count("AAA", "ZZZ")


# PART2
def step_count(source):
    counter, directions_len = 0, len(directions)
    while not source.endswith("Z"):
        source = routes_map[source][directions[counter % directions_len] == "R"]
        counter += 1
    return counter


nodes_ending_with_a = [key for key in routes_map if key.endswith("A")]

part2 = lcm(*[step_count(node) for node in nodes_ending_with_a])
