
# BOJ 1158

def josephus_problem(n, k):
    result_arr = []

    next_index = k - 1
    people_arr = list(range(1, n + 1))

    while people_arr:
        result = people_arr.pop(next_index)
        result_arr.append(result)
        if len(people_arr) != 0:
            next_index = (next_index + (k - 1)) % len(people_arr)

    print("<", ", ".join(map(str, result_arr)), ">", sep='')


n, k = map(int, input().split())
josephus_problem(n, k)



# n, k = map(int, input().split())
# n = 7
# k = 3
# josephus_problem(n, k)
#
# [1, 2, 3, 4, 5, 6, 7]

# <3, 6, 2, 7, 5, 1, 4>