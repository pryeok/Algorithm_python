



#       v     v
# 1 2 3 4 5 6 7 8 9 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# 1 2 3 4 5 6 7 9 8
# 1 2 3 4 6 5 7 8 9
# 1 2 3 4 6 5 7 9 8

# 2 1 3 4 5 6 7 8 9
# 2 1 3 4 5 6 7 9 8
# 2 1 3 4 6 5 7 8 9
# 2 1 3 4 6 5 7 9 8

# 1 3 2 4 5 6 7 8 9
# 1 3 2 4 5 6 7 9 8
# 1 3 2 4 6 5 7 8 9
# 1 3 2 4 6 5 7 9 8

2
# 1 2
# 2 1

3
# 1 2 3
# 1 3 2
# 2 1 3

5
# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 2 1 3 4
# 2 1 4 3





def fibo_dynamic_programming(n, fibo_memo):

    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo

#       v     v
# 1 2 3 4 5 6 7 8 9
seat_count = 9
vip_seat_array = [4, 7]
def get_all_ways_of_theater_seat(total_count, fixed_seat_array):

    # 예전에 만들었던 fibo_dynamic_programming 에서 가져오면 됩니다!
    memo = {
        1: 1,  # 이 문제에서는 Fibo(1) = 1, Fibo(2) = 2 로 시작합니다!
        2: 2
    }

    answer = 1
    count = 0

    for i in range(total_count):
        if i+1 not in fixed_seat_array:
            count += 1
        else:
            answer *= fibo_dynamic_programming(count, memo)
            count = 0

    answer *= fibo_dynamic_programming(count, memo)

    return answer


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))