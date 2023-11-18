# sol

for x in range(1, 11):
    building_num = int(input())
    li = list(map(int, input().split()))
    answer = 0
    for i in range(2, len(li)-2):
        a = li[i-2]
        b = li[i-1]
        c = li[i]
        d = li[i+1]
        e = li[i+2]

        if c > a and c > b and c > d and c > e:
            min_num = min((c-a), (c-b), (c-d), (c-e))
            answer += min_num

    print(f'#{x} {answer}')
