from GCDFunction import gcd

n1 = int(input("첫 번째 정수를 입력하세요:"))
n2 = int(input("두 번째 정수를 입력하세요:"))

print(n1, "과", n2, "의 최대 공약수는", gcd(n1, n2), "입니다.")
