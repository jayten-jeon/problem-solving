class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            count = nums.count(target)
            start = nums.index(target)
            end = start + count - 1
            return [start, end]
        else:
            return [-1, -1]
