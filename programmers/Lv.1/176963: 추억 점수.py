# sol
def solution(name, yearning, photo):
    dict = {}
    answer = []

    for i in range(len(name)):
        dict[name[i]] = yearning[i]

    for pho in photo:
        s = 0
        for j in range(len(pho)):
            if pho[j] in dict:
                s += dict[pho[j]]
        answer.append(s)
    return answer


# sol2
def solution(name, yearning, photo):
    answer = []
    # zip, for문으로 줄인 버전
    dic = {x: y for x, y in zip(name, yearning)}

    for pho in photo:
        s = 0
        for j in range(len(pho)):
            if pho[j] in dic:
                s += dic[pho[j]]
        answer.append(s)
    return answer
