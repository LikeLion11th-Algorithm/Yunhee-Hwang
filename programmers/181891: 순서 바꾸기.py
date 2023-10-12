# 정수 리스트 num_list와 정수 n이 주어질 때, num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.


# sol
def solution(num_list, n):
    return num_list[n::1]+num_list[:n:1]


# sol2
def solution(num_list, n):
    return num_list[n:]+num_list[:n]  # 간격 1이면 별도로 안 써줘도 되겠다
