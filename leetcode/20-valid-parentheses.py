class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        for x in s:
            if x in ['[', '(', '{']:
                q.append(x)
            elif x == ']':
                if not q:
                    return False
                if q[-1] != '[':
                    return False
                q.pop(-1)
            elif x == ')':
                if not q:
                    return False
                if q[-1] != '(':
                    return False
                q.pop(-1)
            elif x == '}':
                if not q:
                    return False
                if q[-1] != '{':
                    return False
                q.pop(-1)
        return not q
