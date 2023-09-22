# 정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

# sol
def solution(num, n):
    return int(bool(num % n == 0))

# sol2


def solution(num, n):
    return int(not (num % n))  # 나머지가 0이면 True, 나머지가 있으면 False 반환
