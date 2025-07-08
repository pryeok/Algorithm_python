

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]



def is_existing_target_number_binary(target, array):
    # 배열의 최솟값
    current_min = 0
    # 배열의 최대값
    current_max = len(array) - 1
    # 현재 예상값 (최솟값과 최대값을 더하고 나누는 것이 포인트)
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2 # while문의 끝에 예상값 잡아줘야 된다

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)