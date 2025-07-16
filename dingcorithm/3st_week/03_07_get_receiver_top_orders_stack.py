

top_heights = [6, 9, 5, 7, 4]

# 스택으로 풀이
def get_receiver_top_orders(heights):

    answer = [0] * len(heights)

    while heights: # 해당 stack이 비어있지 않다면 계속 반복해라 !!
                   # if heights: 랑 같은 코드
                   # heights 값이 있다면 언제나 true

        print("heights", heights)

        height = heights.pop() # 팝을 하면 리스트의 맨 오른쪽 부터 뽑힘
                               # 동시에 리스트의 길이도 1 줄게됨

        for idx in range(len(heights) - 1, -1, -1):

            # print("heights[idx]", heights[idx])
            # print("height", height)
            # print("idx", idx)

            if heights[idx] > height:
                print("len(heights)", len(heights))
                answer[len(heights)] = idx + 1
                # print("answer", answer)
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))