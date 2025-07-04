
input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):

    count_to_all_zero = 0
    count_to_all_one = 0

    # 0과 1 중에 어떤 수가 적은지 선택
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    # 선택된 적은 수를 찾아서 그와 반대되는 수로 변경
    # 1의 수가 더 적은 경우
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    # min : min은 가장 작은 수를 반환
    return min(count_to_all_one, count_to_all_zero)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)