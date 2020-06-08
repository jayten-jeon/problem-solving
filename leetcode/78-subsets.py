from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        for i in range(n+1):
            subsets += [list(comb) for comb in combinations(nums, i)]
        print(subsets)
        return subsets
