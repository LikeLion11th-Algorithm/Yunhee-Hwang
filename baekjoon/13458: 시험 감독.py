# sol

n = int(input())
member = 0
num = []
snum = list(map(int, input().split()))

P, Q = map(int, input().split())

for i in range(n):
    num.append(snum[i] - P)
    member += 1

    if num[i] > 0:
        member += num[i] // Q
        if num[i] % Q != 0:
            member += 1

print(member)
