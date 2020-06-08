class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(target=target, picks= [], candidates=candidates):
            if sum(picks) == target:
                if sorted(picks) not in ans:
                    ans.append(sorted(picks))
                return
            if sum(picks) > target:
                return
            for c in candidates:
                backtrack(target, picks+[c], candidates)
        backtrack()
        return ans
