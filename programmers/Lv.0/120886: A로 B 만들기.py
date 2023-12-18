# sol

def solution(before, after):

    answer1 = sorted(before)
    answer2 = sorted(after)

    return int(bool(answer1 == answer2))
