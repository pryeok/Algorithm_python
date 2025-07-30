


board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]

moves = [1,5,3,5,1,2,1,4]

#   4      3       1        1 3 2 x 4
# [3][0] [1][4]  [1][2]


def solution(board, moves):

    stack = []
    result_count = 0
    cur = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                if len(stack) > 0 and stack[-1] == board[j][i-1]:
                    stack.pop()
                    result_count += 2
                else:
                    stack.append(board[j][i-1])
                board[j][i - 1] = 0
                break

    return result_count


print("정답 = 4 / 현재 풀이 값 = ", solution(board, moves))