class Solution:
    def climbStairs(self, n: int) -> int:
        checks = [0 for _ in range(n)]
        checks[0] = 1
        if n > 1:
            checks[1] = 2
        for i in range(2, n):
            checks[i] = checks[i-1] + checks[i-2]
        return checks[n-1]
