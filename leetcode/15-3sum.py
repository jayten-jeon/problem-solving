from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(target, num_count):
            pairs = []
            for num in num_count or -target >= num:
                if num_count[num] == 0 or -target > num:
                    continue
                num_count[num] -= 1

                if target - num in num_count and num_count[target-num] != 0 and target - num >= num:
                    num_count[target - num] -= 1

                    pairs.append([num, target-num])
                else:
                    num_count[num] += 1
            for num1, num2 in pairs:
                num_count[num1] += 1
                num_count[num2] += 1
            return pairs
            
        triplets = []
        num_count = dict(Counter(sorted(nums)))
        for num in num_count:
            if num_count[num] == 0:
                continue
            num_count[num] -= 1
            triplets += [[num] + pair for pair in two_sum(0 - num, num_count)]
            num_count[num] += 1
        return(triplets)
