def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    possible = ['-', '_', '.']
    check = []

    for i in range(len(new_id)):
        if new_id[i] not in possible:
            if new_id[i].isalpha() or new_id[i].isdigit():
                continue
            else:
                check.append(new_id[i])

    for j in range(len(check)):
        new_id = new_id.replace(check[j], '')

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    if new_id[0] == '.':
        new_id = new_id[1:]

    if len(new_id) >= 1:
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')

    # 5단계
    if new_id == '':
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id[0:14]

    # 7단계
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]

    return new_id
