from itertools import permutations

def is_prime(number):
    if number < 2:
        return False
    for n in range(2, int(number / 2) + 1):
        if number  % n == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    numbers = list(set(int("".join(pair)) for n in range(1, len(numbers) + 1) for pair in list(permutations(numbers, n))))
    answer = sum([is_prime(n) for n in numbers])
    return answer
