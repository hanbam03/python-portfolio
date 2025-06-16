# 간단한 계산기
print("=== 간단한 계산기 ===")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")

choice = input("원하는 연산을 선택하세요 (1-4): ")
num1 = float(input("첫 번째 숫자: "))
num2 = float(input("두 번째 숫자: "))

if choice == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == '3' :
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == '4':
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print("잘못된 선택입니다.")
