import re


def is_valid_id(input_id) -> bool:
    """Validate input id with regular expression.

    Args:
        input_id (str): id that input from user.

    Returns:
        bool: whether input id satisfies the regular expression.
    """
    regex = re.compile("^[a-z0-9-_]{1}([a-z0-9-_][.]{0,1}){1,13}[a-z0-9-_]{1}$")
    if regex.match(input_id) is None:
        return False

    return True


def solution(new_id):
    answer = ""
    if is_valid_id(new_id):
        answer = new_id
        return answer

    return answer


if __name__ == "__main__":
    pass
