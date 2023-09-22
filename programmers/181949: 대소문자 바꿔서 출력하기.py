
# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

# sol
str = input()
new_str = ''

for word in str:
    if word.isupper():
        new_str += word.lower()
    if word.islower():
        new_str += word.upper()

print(new_str)


# sol2
print(input().swapcase())

# sol3
print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))
