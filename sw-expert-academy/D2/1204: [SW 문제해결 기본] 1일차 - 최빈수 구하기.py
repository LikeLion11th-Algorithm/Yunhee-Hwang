# sol

T = int(input())

for i in range(1, T+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    mid_list = [0] * 101
    for j in range(len(num_list)):
        index = num_list[j]
        mid_list[index] += 1
    mid_list.reverse()
    max_num = max(mid_list)
    answer = 100 - mid_list.index(max_num)
    print(f'#{n} {answer}')
