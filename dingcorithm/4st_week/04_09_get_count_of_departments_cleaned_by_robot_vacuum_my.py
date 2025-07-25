
from collections import deque

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# 북쪽이면 dr[0], dr[0]
# 동쪽이면 dr[1], dr[1]
# 남쪽이면 dr[2], dr[2]
# 서쪽이면 dr[3], dr[3]

# 북쪽[0] 일 때는 서쪽으로 dr[3], dr[3] 이동 == (0) -> (3)
# 동쪽[1] 일 때는 서쪽으로 dr[0], dr[0] 이동 == (1) -> (0)
# 남쪽[2] 일 때는 서쪽으로 dr[1], dr[1] 이동 == (2) -> (1)
# 서쪽[3] 일 떄는 서쪽으로 dr[2], dr[2] 이동 == (3) -> (2)

# +2 % 4
# 3이면 -2해서 1
# 1이면 +2해서 3
# 2이면 -2해서 0
# 0이면 +2해서 2


# 6 2 0 -> 25
def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    temp_d = 0
    total_count = 0

    queue = deque([[r, c, d]])

    while queue:
        r, c, d = queue.popleft()
        temp_d = d

        first_time = 0
        second_time = 0

        if room_map[r][c] == 0:
            room_map[r][c] = 2
            total_count += 1

        rotated_d = rotate(temp_d) # 3
        back_d = get_d_index_when_go_back(d)
        back_r = r + dr[back_d]
        back_c = c + dc[back_d]

        print("total_count :: ", total_count)

        # print("rotated_d :: ", rotated_d)
        # print("r :: ", r)
        # print("c :: ", c)
        # print("d :: ", d)
        # print("rotated_d :: ", rotated_d)
        # print(" dr[rotated_d] :: ",  dr[rotated_d])
        # print(" r + dr[rotated_d] :: ",  r + dr[rotated_d])
        # print(" dc[rotated_d] :: ",  dc[rotated_d])
        # print(" c + dc[rotated_d] :: ",  c + dc[rotated_d])
        # print("room_map[r + dr[rotated_d]][c + dc[rotated_d]] :: ", room_map[r + dr[rotated_d]][c + dc[rotated_d]])

        ## 6 1 3
        while room_map[r + dr[rotated_d]][c + dc[rotated_d]] != 0:
            rotated_d = rotate(rotated_d)
            if first_time == 3:
                # print("r + dr[back_d] :: ", r + dr[back_d])
                # print("c + dc[back_d] :: ", c + dc[back_d])
                # print("back_d :: ", back_d)
                # print("room_map[r + dr[back_d]][c + dc[back_d]]111111 :: ", room_map[r + dr[back_d]][c + dc[back_d]])
                rotated_back_d = rotate(d)
                while room_map[back_r + dr[rotated_back_d]][back_c + dc[rotated_back_d]] != 0:
                    # print("d입니다 :: ", d)
                    rotated_back_d = rotate(rotated_back_d)
                    # print("back_d야!! :: ", back_d)
                    # print("room_map[r + dr[back_d]][c + dc[back_d]]22 :: ", room_map[r + dr[back_d]][c + dc[back_d]])
                    if second_time == 3:
                        return total_count
                    second_time += 1
                else:
                    deque.append(queue, [r + dr[back_d], c + dc[back_d], back_d])
                    break
            first_time += 1
        else:
            # 청소할 곳이 0인 경우
            deque.append(queue, [r + dr[rotated_d], c + dc[rotated_d], rotated_d])

        print("=========================================")

        for row in room_map:
            print(row)

        # print(queue)

    return

# 방향 전환
def rotate(temp_d):
    return (temp_d + 3) % 4

# 후진
def get_d_index_when_go_back(d):
    return (d + 2) % 4

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,2,0,current_room_map4))