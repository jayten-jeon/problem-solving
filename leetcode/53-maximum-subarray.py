class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maximums = [0 for _ in range(len(nums))]
        maximums[0] = nums[0]
        maximums[1] = max(maximums[0] + nums[1], nums[1])
        for i, num in enumerate(nums[2:], start=2):
            maximums[i] = max(maximums[i - 1] + num, num)
        print(maximums)
        return max(maximums)
