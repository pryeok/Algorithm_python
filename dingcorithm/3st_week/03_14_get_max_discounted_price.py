

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):

    result = 0
    array1_index = 0
    array2_index = 0

    prices.sort(reverse=True) # [1500000, 30000, 2000]
    coupons.sort(reverse=True) # [40, 20]

    # 900,000
    # 2,4000
    # 2000

    for i in range(len(prices)): # 0 1 2
        if i < len(coupons):
            result += prices[i] * (100 - coupons[i]) // 100
        else:
            result += prices[i]

    return result


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))