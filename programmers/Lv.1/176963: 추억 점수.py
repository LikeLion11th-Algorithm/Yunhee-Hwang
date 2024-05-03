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
    # print(dict)
    return answer
