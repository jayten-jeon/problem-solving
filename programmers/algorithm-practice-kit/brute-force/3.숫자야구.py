from itertools import permutations 

def check_strike_and_ball(real, expect, s, b):
    _s = sum([r == e for r, e in zip(real, expect)])
    _b = sum([1 for e in expect if real.count(e) == 1 and real.index(e) != expect.index(e)])
    return s == _s and _b == b

def solution(baseball):
    answer = 0
    numbers = [str(i) for i in range(1, 10)]
    candidates = [int("".join(pair)) for pair in permutations(numbers, 3)]
    for c in candidates:
        check = [check_strike_and_ball(str(c), str(expect), s, b) for expect, s, b in baseball]
        if sum(check) == len(check):
            answer += 1
    return answer
