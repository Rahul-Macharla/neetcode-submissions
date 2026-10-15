from typing import List
class Solution:
  def longestConsecutive(self, nums: List[int]):
    collection = set(nums)
    max_count = 0
    for number in nums:
      if number - 1 in collection:
        continue
      next_number = number + 1
      count = 1
      while next_number in collection:
        next_number = next_number + 1
        count = count + 1
      if count > max_count:
        max_count = count
    return max_count    