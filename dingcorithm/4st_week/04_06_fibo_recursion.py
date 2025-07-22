


# 피보나치 20번째 수열을 구하세요
input = 100

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765

def fibo_recursion(n):

    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765


# Fibo(4) = Fibo(3) + Fibo(2) = 2 + 1 = 3
# Fibo(5) = Fibo(4) + Fibo(3) = 3 + 2 = 5
# Fibo(6) = Fibo(5) + Fibo(4) = 5 + 3 = 8 .....
# Fibo(n) = Fibo(n - 1) + Fibo(n-2) !!!