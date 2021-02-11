from collections import defaultdict
import heapq
from typing import DefaultDict
import sys


def generate_graph(fares) -> DefaultDict:
    graph = defaultdict(list)
    for node1, node2, fare in fares:
        graph[node1].append((node2, fare))
        graph[node2].append((node1, fare))

    return graph


def calculate_lowest_fares(src: int, graph: DefaultDict):
    fares = defaultdict(lambda: -1)
    queue = [(0, src)]
    while queue:
        fare1, node1 = heapq.heappop(queue)
        if node1 not in fares:
            fares[node1] = fare1
        else:
            continue
        for node2, fare2 in graph[node1]:
            heapq.heappush(queue, (fares[node1] + fare2, node2))

    return fares


def solution(n, s, a, b, fares):
    answer = sys.maxsize

    graph = generate_graph(fares)
    lowest_fares_from_s = calculate_lowest_fares(s, graph)
    for i in range(1, n + 1):
        base_fare = lowest_fares_from_s[i]
        if base_fare < 0:
            continue
        if base_fare >= lowest_fares_from_s[a] and base_fare >= lowest_fares_from_s[b]:
            continue
        if base_fare > answer:
            continue
        lowest_fares_from_i = calculate_lowest_fares(i, graph)
        fare_a = lowest_fares_from_i[a]
        fare_b = lowest_fares_from_i[b]
        if fare_a == -1 or fare_b == -1:
            continue
        total_fare = fare_a + fare_b + base_fare
        answer = min(answer, total_fare)
    return answer
