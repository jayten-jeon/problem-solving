from itertools import combinations

def is_candidate_key(check, attrs, relation):
    for c in check:
        if c & attrs == c:
            return False
    candidate = set([" ".join([r[a] for a in attrs]) for r in relation])
    return len(candidate) == len(relation)

def solution(relation):
    answer = 0
    check = []
    candidate_keys = sum([list(map(set,combinations(range(len(relation[0])), n))) for n in range(1, len(relation[0]) + 1)], [])
    for c in candidate_keys:
        if is_candidate_key(check, c, relation):
            answer += 1
            check.append(c)
    return answer
