def strtime_to_seconds(strtime: str) -> int:
    splitted = strtime.split(":")
    seconds = int(splitted[0]) * 3600 + int(splitted[1]) * 60 + int(splitted[2])
    return seconds


def seconds_to_strtime(seconds: int) -> str:
    strtime = []

    for i in range(2, -1, -1):
        strtime.append(f"{seconds // 60 ** i:02}")
        seconds %= 60 ** i

    return ":".join(strtime)


def solution(play_time, adv_time, logs):
    answer = ""
    play_time = strtime_to_seconds(play_time)
    adv_time = strtime_to_seconds(adv_time)

    total_times = [0] * (play_time + 1)
    for log in logs:
        splitted = log.split("-")
        start = strtime_to_seconds(splitted[0])
        end = strtime_to_seconds(splitted[1])
        total_times[start] += 1
        total_times[end] -= 1
    for i in range(1, play_time):
        total_times[i] += total_times[i - 1]
    for i in range(1, play_time):
        total_times[i] += total_times[i - 1]

    max_time = 0
    max_time_idx = 0
    for i in range(play_time):
        if i >= adv_time:
            time = total_times[i] - total_times[i - adv_time]
        else:
            time = total_times[i]
        if time > max_time:
            max_time = time
            max_time_idx = i

    if max_time_idx - adv_time + 1 <= 0:
        answer = seconds_to_strtime(0)
    else:
        answer = seconds_to_strtime(max_time_idx - adv_time + 1)

    return answer