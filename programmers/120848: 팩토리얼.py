# i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다.
# 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

# sol
from math import factorial


def solution(n):
    answer = 1
    num = 0

    if n == 1:
        return n

    while answer <= n:
        num += 1
        answer *= num

    return num-1


# sol2
def solution(n):
    divider = 0
    while 1:
        divider += 1
        if n/divider < 1:
            break
        else:
            n /= divider
    return divider-1


# sol3


def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
