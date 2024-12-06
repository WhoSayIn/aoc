require 'set'

class Solution
  def initialize(file_path)
    @file_path = file_path
  end

  def part1
    left, right = read_and_split
    left_sorted = left.sort
    right_sorted = right.sort

    left_sorted.zip(right_sorted).sum { |l, r| (l - r).abs }
  end

  def part2
    left, right = read_and_split
    right_count = right.tally

    left.sum { |l| l * right_count.fetch(l, 0) }
  end

  private

  def read_and_split
    left = []
    right = []
    File.foreach(@file_path) do |line|
      l, r = line.split.map(&:to_i)
      left << l
      right << r
    end
    [left, right]
  end
end

solution = Solution.new('2024/01/input.txt')
puts solution.part1
puts solution.part2
