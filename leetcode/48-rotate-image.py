class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 
        n = len(matrix)
        tmp = []
        for i in range(n):
            col = list(reversed([row[i] for row in matrix]))
            tmp.append(col)
        for y, row in enumerate(tmp):
            for x, num in enumerate(row):
                matrix[y][x] = num
