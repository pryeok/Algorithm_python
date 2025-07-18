

def is_correct_parenthesis(string):

    stack = []

    for i in range(len(string)):

        if string[i] == "(":
            stack.append("(")
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) > 0:
        return False
    else:
        return True

####################################################

    # cur = 0
    #
    # for str in string:
    #     if str == "(":
    #         cur += 1
    #     else:
    #         cur -= 1
    #
    # if cur == 0:
    #     return True
    # else:
    #     return False


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))