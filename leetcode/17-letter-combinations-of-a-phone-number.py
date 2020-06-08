class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combs = []
        alphas = [chr(ord('a') + i) for i in range(26)]
        d2c = dict()
        for x in range(2, 10):
            if x in [7, 9]:
                d2c[str(x)] = alphas[:4]
                alphas = alphas[4:] 
            else:
                d2c[str(x)] = alphas[:3]
                alphas = alphas[3:] 
        chars = [d2c[d] for d in list(digits)]
        
        def make_combs(n, target, chars, comb):
            if n == target:
                combs.append(comb)
                return
            for c in chars[n]:
                make_combs(n + 1, target, chars, comb + c)
        make_combs(0, len(digits), chars, '')
        return combs
