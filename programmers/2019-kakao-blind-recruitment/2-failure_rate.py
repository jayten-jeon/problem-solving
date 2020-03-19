def get_failure_rate(n,stages):
    fail = stages.count(n)
    reach = sum([s >= n for s in stages])
    if reach == 0:
        return 0
    return fail / reach

def solution(N, stages):
    answer = []
    failure_rates = [(n, get_failure_rate(n, stages)) for n in range(1, N + 1)]
    answer = [x[0] for x in sorted(failure_rates, reverse=True, key = lambda x: x[1])]
    return answer
