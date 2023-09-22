# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.


# sol
def solution(number, n, m):
    if (number % n == 0) and (number % m == 0):
        answer = 1
    else:
        answer = 0
    return answer

# sol2


def solution(number, n, m):
    return int(bool((number % n == 0) and (number % m == 0)))

# and랑 &랑 다른데 차이점 알아두기
