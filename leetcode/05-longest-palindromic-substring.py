class Solution:
    def expand(self, s, left, right):
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
        
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - int((max_len - 1) / 2)
                end = i + int(max_len / 2)
        return s[start:end+1]
