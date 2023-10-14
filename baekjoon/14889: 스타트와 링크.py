# sol
from itertools import combinations

# input 숫자 받기
n = int(input())
nums = [i for i in range(n)]

# 능력치 담아둘 이차원 배열 만들고 할당
S = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    S[i] = list(map(int, input().split()))

# 숫자 2가지 조합 뽑기
# list()로 리스트 만드는 거랑 [] 이렇게 리스트 만드는거랑 다르니까 주의하기. 여기에선 list()만 가능
teams = list(combinations(nums, n//2))


# 최소 능력치 차이 초기화
min_diff = float('inf')  # 값을 무한대로 초기화하여 어떤 숫자를 만나도 그 숫자가 더 작은 숫자가 될 수 있도록 함

for team in teams:
    Stark = 0
    Link = 0

    for player in team:
        for other_player in team:
            if player != other_player:
                Stark += S[player][other_player]

    other_team = set(nums)-set(team)
    other_team = list(other_team)

    for player in other_team:
        for other_player in other_team:
            if player != other_player:
                Link += S[player][other_player]

    diff = abs(Stark - Link)
    min_diff = min(min_diff, diff)

print(min_diff)
