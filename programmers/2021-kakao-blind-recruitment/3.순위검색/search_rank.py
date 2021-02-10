from typing import List


# TODO: 효율성 통과를 위해 그룹화 하는 코드 작성


def generate_db(info) -> List:
    return [i.split() for i in info]


def search(query: List, db: List) -> List:
    score = int(query[-1])
    candidate = [raw for raw in db if int(raw[-1]) >= score]

    for i, q in enumerate(query[:-1]):
        if q == "-":
            continue
        candidate = [raw for raw in candidate if raw[i] == q]
    return candidate


def solution(info, query):
    answer = []
    db = generate_db(info)
    query = [q.replace("and", "").split() for q in query]
    answer = [len(search(q, db)) for q in query]
    return answer