from typing import Dict, List, Tuple
from collections import deque, defaultdict
from itertools import permutations
import sys

N = 4


def generate_card_postion_dict(board: List[List[int]]) -> Dict[int, List[Tuple[int]]]:
    card_position_dict = defaultdict(list)
    for y in range(N):
        for x in range(N):
            if board[y][x] == 0:
                continue
            card_position_dict[board[y][x]].append((x, y))
    return card_position_dict


def get_next_nodes(board: List[Tuple[int]], node: Tuple[int]) -> List[Tuple[int]]:
    x, y = node
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    next_nodes = set()
    for d_x, d_y in directions:
        n_x = x + d_x
        n_y = y + d_y
        if n_x < 0 or n_x == N or n_y < 0 or n_y == N:
            continue
        if board[n_y][n_x] == 0:
            next_nodes.add((n_x, n_y))
        while n_x >= 0 and n_x <= N - 1 and n_y >= 0 and n_y <= N - 1:
            if board[n_y][n_x] != 0:
                next_nodes.add((n_x, n_y))
                break
            if (
                (n_y == 0 and n_x == x)
                or (n_y == N - 1 and n_x == x)
                or (n_x == 0 and n_y == y)
                or (n_x == N - 1 and n_y == y)
            ):
                next_nodes.add((n_x, n_y))
            n_x += d_x
            n_y += d_y

    return next_nodes


def move(src: Tuple[int], dst: Tuple[int], board: List[List[int]]) -> List[Tuple[int]]:
    queue = deque([(src, [src])])
    visited = []
    while queue:
        node, path = queue.popleft()
        if node == dst:
            return path
        if node in visited:
            continue
        visited.append(node)
        next_nodes = get_next_nodes(board, node)
        queue.extend([(node, path + [node]) for node in next_nodes])


def solution(board: List[List[int]], r: int, c: int) -> int:
    """
    - 카드는 1~6 까지 2쌍씩 존재.
    - 하지만 1~6 전체가 존재하진 않으니 n개라고 가정하면, 총 n! 개의 경우의 수가 있음
    - 각 경우의 수에서 카드쌍 마다 총 2개가 존재하니, 어떤 카드에서 부터 시작하는 것이 최단 경로인지 2가지가 존재
    - 위치마다 이동할 수 있는 가짓수는 4(상하좌우) ~ 8(상하좌우 + 컨트롤 상하좌우)개가 존재

    - 구현할 함수
        - 4 x 4 board 에서 각 각 이동할 수 있는 위치를 계산하는 함수
        - 출발 좌표, 도착 좌표가 주어지면, 최단 경로를 반환하는 함수
        - 카드의 위치를 기록하는 함수
    Args:
        board (List[int]):
            0: 카드가 제거된 빈칸
            1~6: 2쌍 존재, 같은 숫자는 같은 그림의 카드를 의미
        r (int): 최초 커서의 세로 위치
        c (int): 최초 커서의 가로 위치

    Returns:
        int: Minimum number of key operation
    """
    answer = sys.maxsize

    cards = set(sum(board, [])) - {0}
    cards_permutations = permutations(cards, len(cards))
    card_position_dict = generate_card_postion_dict(board)
    min_path = []
    for cards in cards_permutations:
        path = []
        current = (c, r)
        temp = [row.copy() for row in board]
        for card in cards:
            path_a, path_b = [], []
            card_a, card_b = card_position_dict[card]
            path_a = move(current, card_a, temp) + move(card_a, card_b, temp)
            path_b = move(current, card_b, temp) + move(card_b, card_a, temp)
            temp[card_a[1]][card_a[0]] = 0
            temp[card_b[1]][card_b[0]] = 0
            if len(path_a) < len(path_b):
                path += path_a
                current = card_b
            else:
                path += path_b
                current = card_a
        if answer > len(path):
            answer = len(path)
            min_path = path
    return answer
