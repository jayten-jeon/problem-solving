class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for str in strs:
            ans.setdefault(tuple(sorted(str)), [])
            ans[tuple(sorted(str))].append(str)        
        return ans.values()
