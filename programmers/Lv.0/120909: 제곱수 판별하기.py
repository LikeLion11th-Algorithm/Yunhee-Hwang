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

    return 1 if n == (n**0.5)*(n**0.5) else 2
