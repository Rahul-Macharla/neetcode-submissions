from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        frequency = Counter(nums)
        max_reps = frequency.most_common(k)
        result = []
        for num, frequency in max_reps:
            result.append(num)
        return(result)