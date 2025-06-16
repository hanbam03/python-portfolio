import random

print("=== 숫자 맞추기 게임 ===")
print("1부터 100 사이의 숫자를 맞춰보세요!")

# 컴퓨터가 랜덤 숫자 생성
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print(f"기회는 {max_attempts}번입니다!")

while attempts < max_attempts:
    try:
        guess = int(input("숫자를 입력하세요: "))
        attempts += 1
        
        if guess == secret_number:
            print(f"축하합니다! {attempts}번 만에 맞췄습니다!")
            print(f"정답은 {secret_number}였습니다!")
            break
        elif guess < secret_number:
            print("더 큰 숫자입니다!")
        else:
            print("더 작은 숫자입니다!")
            
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"남은 기회: {remaining}번")
        
    except ValueError:
        print("숫자만 입력해주세요!")
        attempts -= 1  # 잘못된 입력은 기회 차감 안함

if attempts == max_attempts and guess != secret_number:
    print(f"게임 오버! 정답은 {secret_number}였습니다.")
