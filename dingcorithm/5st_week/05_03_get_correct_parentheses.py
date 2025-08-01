from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_parentheses(string):  # 올바른 괄호인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack: # 스택이 비어있지 않은 경우에만 pop 할 수 있게 해줌!!
            stack.pop()
    return len(stack) == 0


def separate_to_u_v(string):  # u, v로 분리
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:  # 큐사용
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:  # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 합니다. 즉, 여기서 괄 쌍이 더 생기면 안됩니다.
            break

    v = ''.join(list(queue))
    return u, v


def reverse_parentheses(string):  # 뒤집기
    reversed_string = ""
    print("string :", string)
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string


def change_to_correct_parentheses(string):
    if string == '':  # 1번
        return ''
    u, v = separate_to_u_v(string)  # 2번
    print("u :", u)
    print("v :", v)
    if is_correct_parentheses(u):  # 3번
        print("u ::", u)
        return u + change_to_correct_parentheses(v)
    else:  # 4번
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)


# print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

# print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
# print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))