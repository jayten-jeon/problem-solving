class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        end = 0
        n = len(s)
        chars = set()
        while start < n and end < n:
            if s[end] not in chars:
                chars.add(s[end])
                end += 1
            else:
                longest = max(len(chars), longest)
                chars.remove(s[start])
                start += 1
        longest = max(len(chars), longest)
        return longest
