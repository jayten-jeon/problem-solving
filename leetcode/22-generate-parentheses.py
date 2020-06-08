class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtracking(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtracking(S+'(', left + 1, right)
            if right < left:
                backtracking(S + ')', left, right + 1)
        backtracking()
        return ans
