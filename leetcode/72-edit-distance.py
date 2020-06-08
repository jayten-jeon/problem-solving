class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for x in range(m+1):
            table[0][x] = x
        for y in range(n+1):
            table[y][0] = y
        for y, c2 in enumerate(word2, start=1):
            for x, c1 in enumerate(word1, start=1):
                if c1 == c2:
                    table[y][x] = table[y-1][x-1]
                else:
                    table[y][x] = min(table[y-1][x], table[y][x-1], table[y-1][x-1]) + 1
                # print(c1, c2, table[y][x])
        print(table)
        return table[-1][-1]
