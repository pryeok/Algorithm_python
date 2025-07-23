

from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    cony_queue = deque()
    brown_queue = deque()
    queue = deque()

    queue.append((brown_loc, 0))
    print(queue)






    return


print(catch_me(c, b))  # 5가 나와야 합니다!

# print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
# print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
# print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))


# 11 2

# 11+1=12, 2-1=1, 2+1=3, 2*2=4
# 11+3=14, 1-1=0, 1+1=2, 1*2=2 | 3-1=2, 3+1=4, 3*2=6 | 4-1=3, 4+1=5, 4*2=8
# 11+6=17,
# 11+10=21, 16*2=32
# 11+15=26, 32*2=64

# 10 3
# 10+1=11, 3*2=6
# 11+3=14, 6*2=12
# 14+6=20, 12*2=24
# 20+10=21, 16*2=32
# 21+15=36, 32-1=31


