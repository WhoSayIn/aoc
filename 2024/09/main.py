class Solution:
    def __init__(self, file_path="2024/09/input.txt"):
        with open(file_path) as f:
            self.input = [int(i) for i in f.read().strip()]

    def _checksum(self, disk):
        return sum(i * b for i, b in enumerate(disk))

    def _strip(self, disk):
        while disk[-1] == ".":
            disk.pop()

    def part1(self):
        disk = []
        pos = 0
        for i, l in enumerate(self.input):
            if i % 2 == 0:
                disk += l * [pos]
                pos += 1
            else:
                disk += l * ["."]

        empty = [i for i, b in enumerate(disk) if b == "."]

        for i in empty:
            self._strip(disk)

            if i < len(disk):
                disk[i] = disk[-1]
                disk.pop()

        return self._checksum(disk)


if __name__ == "__main__":
    s = Solution()
    print(s.part1())
