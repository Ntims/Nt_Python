def f (n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result

m = int (input("숫자 입력:"))
print(f(m))
print(f(3)*2+f(5))
