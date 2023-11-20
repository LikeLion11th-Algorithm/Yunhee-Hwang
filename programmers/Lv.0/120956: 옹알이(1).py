# sol

def solution(babbling):
    answer = 0
    possible_pro = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        for a in possible_pro:
            b = b.replace(a, '*')

        b = b.replace('*', '')
        if len(b) == 0:
            answer += 1

    return answer
