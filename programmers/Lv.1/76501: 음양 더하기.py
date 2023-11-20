# sol
def solution(absolutes, signs):

    result = 0

    for i in range(len(absolutes)):
        if signs[i] == bool(0):
            result -= absolutes[i]

        if signs[i] == bool(1):
            result += absolutes[i]

    return result


# sol2
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
