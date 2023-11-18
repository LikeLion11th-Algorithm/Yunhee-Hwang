# sol

n = int(input())

for i in range(n):
    num_list = list(map(int, input().split()))
    answer = 0
    for j in range(len(num_list)):
        if num_list[j] % 2 == 1:
            answer += num_list[j]
    print(f'#{i+1} {answer}')
