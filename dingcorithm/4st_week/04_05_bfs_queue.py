
## Queue으로 BFS 풀이

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):

    queue = [start_node]
    visited = []  # 방문한 걸 저장하기 위한 배열

    while queue:
        cur_index = queue.pop(0) # 큐를 뺄때는 pop(0)으로 빼기!!
        visited.append(cur_index)
        for adjacent_node in adj_graph[cur_index]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!

  # curindex  que   visited
  #    0       1       0
  #    1     2 3 4     1
  #    2   3 4 5 6 7   2
  #    3    4 5 6 7    3
  #    4    5 6 7 8    4
  #    5    6 7 8 9    5