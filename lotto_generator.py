import random

print("=== 로또 번호 생성기 ===")
print("행운의 로또 번호를 생성해드립니다!")

def generate_lotto_numbers():
    """로또 번호 6개를 생성하는 함수"""
    numbers = random.sample(range(1, 46), 6)  # 1~45 중 6개 선택
    numbers.sort()  # 오름차순 정렬
    return numbers

def generate_multiple_sets(count):
    """여러 세트의 로또 번호 생성"""
    print(f"\n🎲 {count}세트의 로또 번호를 생성합니다!")
    print("-" * 30)
    
    for i in range(count):
        numbers = generate_lotto_numbers()
        print(f"{i+1}번째: {numbers}")

# 메인 프로그램
while True:
    print("\n1. 로또 번호 1세트 생성")
    print("2. 로또 번호 여러 세트 생성")
    print("3. 종료")
    
    choice = input("\n선택하세요 (1-3): ")
    
    if choice == '1':
        numbers = generate_lotto_numbers()
        print(f"\n🍀 행운의 번호: {numbers}")
        
    elif choice == '2':
        try:
            count = int(input("몇 세트를 생성할까요? "))
            if count > 0:
                generate_multiple_sets(count)
            else:
                print("1 이상의 숫자를 입력해주세요!")
        except ValueError:
            print("숫자만 입력해주세요!")
            
    elif choice == '3':
        print("행운을 빕니다! 👋")
        break
        
    else:
        print("1, 2, 3 중 하나를 선택해주세요!")
