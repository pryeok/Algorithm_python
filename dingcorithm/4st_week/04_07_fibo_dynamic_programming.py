
# 피보나치의 기본 정의
# F(n) = F(n-1) + F(n-2)

input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

## 내가 풀어본 문제 (이거는 사실 반복문식) -> O(n)
def fibo_dynamic_programming(n, fibo_memo):

    cur_index = 3
    while cur_index <= n:
        if cur_index not in fibo_memo:
            fibo_memo[cur_index] = fibo_memo[cur_index-2] + fibo_memo[cur_index-1]
        cur_index += 1

    return fibo_memo[n]


## 정답 (재귀 + 메모이제이션 방식) -> O(n)
# def fibo_dynamic_programming(n, fibo_memo):
#
      # fibo_dynamic_programming(n)을 호출해서 결과를 저장해놨다면, 다시 계산하지 않고 바로 꺼내는 중복 계산을 막아주는 핵심 포인트!!!
#     if n in fibo_memo:
#         return fibo_memo[n]
#
#     nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
#     fibo_memo[n] = nth_fibo
#     return nth_fibo

print(fibo_dynamic_programming(input, memo))


