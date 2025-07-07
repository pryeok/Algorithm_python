
def find_max_occurred_alphabet(string):

    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not(char.isalpha()):
            continue
        arr_index = ord(char) - ord('a')



    return "a"


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


print("==========================")
