# sol
import math


def solution(n):

    num = int(math.sqrt(n))
    if num*num == n:
        return 1
    else:
        return 2


# sol2
def solution(n):

    return 1 if (n**0.5).is_integer() else 2
