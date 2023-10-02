# 문제는 노션 확인

# my sol - 틀림
# 문제의 조건 중 '모든 사람이 모험을 떠나지 않아도 된다'는 부분 간과하여 모든 사람이 그룹을 형성하도록 함
# 공포도가 낮은 사람부터 그 사람의 공포도만큼 그룹원 결성 시 더 많은 그룹 생성 가능
N = input()

people = list(map(int, input().split()))

people.sort()
people.reverse()

groups = 0
people_num = len(people)

for i in range(people_num):
    if people[i] <= people_num:
        groups += 1
        people_num -= people[i]
    if people[i] > people_num:
        print(groups)


# sol-example
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면
        result += 1  # 총 그룹의 수 증가시키기
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력
