# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

# sol
def solution(num_list):

    x = 1
    y = 0

    for num in num_list:
        x *= num
        y += num

    if x < y*y:
        return 1

    else:
        return 0

# else 문 처리 안 해도 됨


def solution(num_list):

    x = 1
    y = 0

    for num in num_list:
        x *= num
        y += num

    if x < y*y:
        return 1
    return 0
