class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        counts = [[0 for _ in range(m)] for _ in range(n)]
        counts[0][0] = 1
        for y in range(n):
            for x in range(m):
                if y == 0 and x == 0:
                    continue
                if x > 0:
                    counts[y][x] += counts[y][x-1]
                if y > 0:
                    counts[y][x] += counts[y-1][x]
        return counts[-1][-1]
