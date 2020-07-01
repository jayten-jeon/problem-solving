class Solution:
    def countSubstrings(self, s: str) -> int:
        checks = dict()
        def isPalindrom(str):
            if str in checks:
                return True
            n = len(str)
            start = 0
            end = n -1
            while start <= end:
                if str[start] != str[end]:
                    return False
                start += 1
                end -= 1  
            checks[str] = True
            return True
        ans = 0
        n = len(s)
        
        for i in range(n):
            for j in range(i+1, n+1):
                substr = s[i:j]
                if isPalindrom(substr):
                    ans += 1
        return ans
