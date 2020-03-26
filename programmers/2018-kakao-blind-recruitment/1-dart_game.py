import re

def solution(dartResult):
    answer = 0
    pattern = "([0-9]|10)([S|D|T])([*|#]?)"
    darts = re.findall(pattern, dartResult)
    scores = []
    for i, (score, bonus, option) in enumerate(darts):
        score = int(score)
        if bonus == 'D':
            scores.append(pow(score, 2))
        elif bonus == 'T':
            scores.append(pow(score, 3))
        else:
            scores.append(score)
        if option == '*':
            scores[i] *= 2
            if i > 0:
                scores[i - 1] *= 2
        elif option == '#':
            scores[i] *= -1
    answer = sum(scores)
    return answer
