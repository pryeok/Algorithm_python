from collections import deque

prices = [1, 2, 3, 2, 3]

def get_price_not_fall_periods(prices):

    result = []
    prices = deque(prices) # deque 메서드를 통해서 prices 리스트를 Queue 형태로 변환!!!!

    while prices: # 해당 queqe가 비어있지 않다면 계속 반복해라 !!

        cur = prices.popleft()
        index = 0

        for i in prices:
            if cur <= i:
                index += 1
            else:
                index += 1
                break
        result.append(index)

    return result


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))