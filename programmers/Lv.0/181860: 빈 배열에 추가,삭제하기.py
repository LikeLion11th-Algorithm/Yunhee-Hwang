# sol

def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if bool(flag[i]) == 1:
            for j in range(arr[i]):
                X.append(arr[i])
                X.append(arr[i])

        else:
            for j in range(arr[i]):
                del X[-1]
    return X


# sol2
def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if bool(flag[i]) == 1:
            for j in range(arr[i]*2):
                X.append(arr[i])

        else:
            for j in range(arr[i]):
                del X[-1]
    return X


# sol3
def solution(arr, flag):
    X = []
    for i, f in enumerate(flag):
        if f:
            X += [arr[i]] * (arr[i]*2)
        else:
            for _ in range(arr[i]):
                X.pop()
    return X
