from typing import List
from itertools import combinations
from collections import Counter


def generate_course(orders, n_courses) -> List[str]:
    course = []
    for n in n_courses:
        candidate = [
            "".join(sorted(list(c))) for order in orders for c in combinations(order, n)
        ]
        counter = Counter(candidate)
        if not counter:
            continue
        _, top_count = counter.most_common(1)[0]
        if top_count < 2:
            continue
        course += [k for k, v in counter.most_common() if v == top_count]

    return sorted(course)


def solution(orders, course):
    answer = generate_course(orders, course)
    return answer