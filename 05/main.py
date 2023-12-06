from collections import defaultdict
from functools import cache


class Solution:
    def __init__(self):
        self.m = float("inf")
        file = open("05/input.txt").read().strip()
        groups = file.split("\n\n")
        self.seeds = [int(seed) for seed in groups[0].split(": ")[1].split()]
        self.groups_processed = defaultdict(dict)

        for group in groups[1:]:
            header, *rows = group.split("\n")
            source, destination = header.split()[0].split("-to-")

            conditions = []
            for row in rows:
                drs, srs, rl = [int(r) for r in row.split()]
                conditions.append([srs, srs + rl - 1, drs - srs])

            self.groups_processed[source][destination] = conditions

    def part1(self):
        return min(self._get_location_from_seed(seed) for seed in self.seeds)

    def _get_location_from_seed(self, seed):
        group = "seed"

        while group != "location":
            group, seed = self._get_target_from_seed(seed, group)

        if group == "location":
            self.m = min(self.m, seed)

        return seed, group

    @cache
    def _get_target_from_seed(self, seed, source):
        target_name = list(self.groups_processed[source].keys())[0]

        result = seed
        for range_start, range_end, delta in self.groups_processed[source][target_name]:
            if range_start <= seed <= range_end:
                return target_name, delta + seed

        return target_name, result


if __name__ == "__main__":
    s = Solution()
    print(s.part1())
