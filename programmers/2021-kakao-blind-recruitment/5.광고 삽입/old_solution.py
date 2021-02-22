# coding=utf-8
# This is a sample Python script.


def solution(play_time, adv_time, logs):
    logs = preprocess_logs(logs)

    acc_view = 0
    max_view = (0, 1)
    max_view_start = "00:00:00"
    adv_time = convert_time(adv_time)
    play_time = convert_time(play_time)
    for i, log in enumerate(logs):
        current_view = (0, 1)
        adv_start_time = log[0]
        adv_end_time = adv_start_time + adv_time
        if adv_end_time > play_time:
            break
        for next_log in logs[i:]:
            for x in next_log[:2]:
                if x >= adv_start_time and x <= adv_end_time:
                    current_view += (adv_end_time - x, 1)
                    break
                if x >= adv_start_time and x <= adv_end_time:
                    current_view += (adv_end_time - x, 1)
            if max_view < current_view:
                max_view = current_view
                max_view_start = log[2]
    return max_view_start


def convert_time(time):
    split = list(map(int, time.split(":")))

    return split[0] * 3600 + split[1] * 60 + split[2]


def preprocess_logs(logs):
    new_logs = []
    for log in logs:
        split = log.split("-")
        new_logs.append([convert_time(x) for x in split] + [split[0]])
        new_logs.sort(key=lambda x: x[0])
    return new_logs


# play_time	adv_time	logs	result
assert (
    solution(
        "02:03:55",
        "00:14:15",
        [
            "01:20:15-01:45:14",
            "00:40:31-01:00:00",
            "00:25:50-00:48:29",
            "01:30:59-01:53:29",
            "01:37:44-02:02:30",
        ],
    )
    == "01:30:59"
)
assert (
    solution(
        "99:59:59",
        "25:00:00",
        [
            "69:59:59-89:59:59",
            "01:00:00-21:00:00",
            "79:59:59-99:59:59",
            "11:00:00-31:00:00",
        ],
    )
    == "01:00:00"
)
assert (
    solution(
        "50:00:00",
        "50:00:00",
        ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"],
    )
    == "00:00:00"
), solution(
    "50:00:00",
    "50:00:00",
    ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"],
)

# solution("02:03:55",	"00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])