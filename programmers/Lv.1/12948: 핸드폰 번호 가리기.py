def solution(phone_number):
    secured_number = ((len(phone_number)-4)*'*')+phone_number[-4:]
    return secured_number
