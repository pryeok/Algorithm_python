
finding_target = 7
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

6

def is_exist_target_number_binary(target, array):

    # 배열의 최솟값
    current_min = 0
    # 배열의 최대값
    current_max = len(array) - 1
    # 현재 예상값 (최솟값과 최대값을 더하고 나누는 것이 포인트)
    current_guess = (current_min + current_max) // 2 # 3

    while current_min <= current_max:
        if array[current_guess] == target:
            return True

        else:
            for result in range(finding_target, current_guess):
                if target != array[result]:
                    current_min = current_guess + 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)