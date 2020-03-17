def get_score(pattern, answers):
    n = len(pattern)
    m = len(answers)
    pattern = pattern * int(m / n) + pattern[:int(m % n)]
    return sum([p == a for p, a in zip(pattern, answers)])

def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [get_score(pattern1, answers), get_score(pattern2, answers), get_score(pattern3, answers)]
    max_score = max(scores)
    answer = [i+1 for i, s in enumerate(scores) if s == max_score]
    return answer
