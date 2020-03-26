def solution(bridge_length, weight, truck_weights):
    second = 1;
    N = len(truck_weights)
    passing = []
    seconds = []
    passed = []
    while len(passed) < N:
        if len(truck_weights) > 0:
            truck = truck_weights[0]
            if sum(passing) + truck <= weight:
                passing.append(truck_weights.pop(0))
                seconds.append(0)
        seconds = [s + 1 for s in seconds]
        for i, s in enumerate(seconds):
            if s == bridge_length:
                passed.append(passing.pop(i))
                seconds.pop(i)
        second += 1

    return second
