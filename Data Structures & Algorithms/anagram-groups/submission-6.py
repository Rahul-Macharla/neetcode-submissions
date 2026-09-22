from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        basket = defaultdict(list)
        for word in strs:
            sorted_strs = ''.join(sorted(word))
            basket[sorted_strs].append(word)
        return(list(basket.values()))
        