from collections import deque

while True:
    stack = deque()
    sentence = input()
    if sentence == '.':
        break

    for i in sentence:
        if i == '.':
            if len(stack) == 0:
                print('yes')
                break
            else:
                print('no')
                break

        if i == '(' or i == '[':
            stack.append(i)

        if i == ')':
            if len(stack) == 0:
                print('no')
                break

            elif stack[-1] == "(":
                stack.pop()

            elif stack[-1] != "(":
                print('no')
                break

        if i == ']':
            if len(stack) == 0:
                print('no')
                break
            elif stack[-1] == "[":
                stack.pop()

            elif stack[-1] != '[':
                print('no')
                break
