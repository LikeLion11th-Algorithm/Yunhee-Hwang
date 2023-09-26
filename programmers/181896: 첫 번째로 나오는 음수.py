
# 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요.
# 음수가 없다면 -1을 return합니다.

# sol
def solution(num_list):

    answer = -1

    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            break  # break 안 쓰면 첫번째로 나오는 음수가 아니라 마지막에 나온 음수

    return answer


# sol2
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1
