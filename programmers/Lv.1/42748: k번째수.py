# sol1
def solution(array, commands):

    for i in range(1, len(commands)+1):
        new_list = []
        k = commands[i-1][2]
        # print("k=",k)
        for j in range(commands[i-1][0]-1, commands[i-1][1]):
            new_list.append(array[j])
            # print(new_list)

        new_list.sort()
        answer.append(new_list[k-1])

    return answer


# sol2
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        l = sorted(array[i-1:j])
        answer.append(l[k-1])

    return answer


# sol3
def solution(array, commands):

    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
