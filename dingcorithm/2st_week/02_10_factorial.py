

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1) # 이 부분이 포인트

print(factorial(60))




# def factorial(n):
#     result = n
#     for numb in range(5-1, 0, -1):
#         result = result * numb
#
# print(factorial(5))