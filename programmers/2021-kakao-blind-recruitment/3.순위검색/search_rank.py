from typing import List
from collections import defaultdict
import bisect

# TODO: 효율성 통과를 위해 그룹화 하는 코드 작성

db = defaultdict(list)


def generate_raw(info: List, idx: int, columns: List):
    global db

    if idx == len(info) - 1:
        key = " and ".join(columns)
        bisect.insort(db[key], int(info[-1]))
        return

    generate_raw(info, idx + 1, columns + [info[idx]])
    generate_raw(info, idx + 1, columns + ["-"])


def generate_db(infos: List):
    global db

    for info in infos:
        generate_raw(info.split(), 0, [])


def search(query: List, db: List) -> List:
    candidate = db[query[0]]
    i = bisect.bisect_left(candidate, query[1])

    return len(candidate) - i


def solution(info, query):
    answer = []
    generate_db(info)
    query = [(" ".join(q.split()[:-1]), int(q.split()[-1])) for q in query]
    answer = [search(q, db) for q in query]
    return answer