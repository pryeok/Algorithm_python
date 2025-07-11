

# 병합정렬
array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    while array1_index < len(array1):
        result.append(array1[array1_index])
        array1_index += 1

    while array2_index < len(array2):
        result.append(array2[array2_index])
        array2_index += 1

        return result


print(merge(array_a, array_b))

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1, 2, 3, 5, 40], [10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1, -1, 0], [1, 6, 9, 10]))



# [1, 2, 3, 5]  # 정렬된 배열 A
# [4, 6, 7, 8]  # 정렬된 배열 B
# [] # 두 집합을 합칠 빈 배열 C
#
#
#         ↓
# 1단계 : [1, 2, 3, 5]
#         ↓
#        [4, 6, 7, 8]
#         1과 4를 비교합니다!
#         1 < 4 이므로 1을 C 에 넣습니다.
#      C:[1]
#
#            ↓
# 2단계 : [1, 2, 3, 5]
#         ↓
#        [4, 6, 7, 8]
#         2와 4를 비교합니다!
#         2 < 4 이므로 2를 C 에 넣습니다.
#      C:[1, 2]
#
#
#               ↓
# 3단계 : [1, 2, 3, 5]
#         ↓
#        [4, 6, 7, 8]
#         3과 4를 비교합니다!
#         3 < 4 이므로 3을 C 에 넣습니다.
#      C:[1, 2, 3]
#
#                  ↓
# 4단계 : [1, 2, 3, 5]
#         ↓
#        [4, 6, 7, 8]
#         5와 4를 비교합니다!
#         5 > 4 이므로 4을 C 에 넣습니다.
#      C:[1, 2, 3, 4]
#
#                  ↓
# 5단계 : [1, 2, 3, 5]
#            ↓
#        [4, 6, 7, 8]
#         5와 6을 비교합니다!
#         5 < 6 이므로 5을 C 에 넣습니다.
#      C:[1, 2, 3, 4, 5]
#
# 엇, 이렇게 되면 A 의 모든 원소는 끝났습니다!
#
# 그러면 B에서 안 들어간 원소인
#        [6, 7, 8] 은 어떡할까요?
# 하나씩 C 에 추가해주면 됩니다.
#      C:[1, 2, 3, 4, 5, 6, 7, 8] 이렇게요!
#
# 그러면 A 와 B를 합치면서 정렬할 수 있었습니다.