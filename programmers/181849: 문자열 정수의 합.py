# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

# sol
def solution(num_str):
    answer = 0

    for i in range(len(num_str)):
        answer += int(num_str[i])

    return answer

# my sol2


def solution(num_str):
    return sum(map(int, num_str))
