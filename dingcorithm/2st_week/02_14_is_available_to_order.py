shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 내가 풀어본 문제
def is_available_to_order(menus, orders):

    menus.sort()

    # 배열의 최솟값
    current_min_menu = 0
    # 배열의 최대값
    current_max_menu = len(menus) - 1
    # 현재 예상값 (최솟값과 최대값을 더하고 나누는 것이 포인트)
    current_guess_menu = (current_min_menu + current_max_menu) // 2 # 2

    order_num = 0

    while current_min_menu <= current_max_menu:
        if order_num == len(orders):
                return True
        elif menus[current_guess_menu] == orders[order_num]:
                order_num += 1
                current_min_menu = 0
                current_max_menu = len(menus) - 1
        elif menus[current_guess_menu] < orders[order_num]:
            current_min_menu = current_guess_menu + 1
        elif menus[current_guess_menu] > orders[order_num]:
            current_max_menu =  current_guess_menu - 1
        current_guess_menu = (current_min_menu + current_max_menu) // 2

    return False

# 개선답안_1 (target인 1개의 값을 찾는 메서드로 처리)
# def is_available_to_order(menus, orders):
#     menus.sort()  # menus 정렬!
#     for order in orders:
#         if not is_existing_target_number_binary(order, menus):
#             return False
#     return True
#
#
# def is_existing_target_number_binary(target, array):
#     current_min = 0
#     current_max = len(array) - 1
#     current_guess = (current_min + current_max) // 2
#
#     while current_min <= current_max:
#         if array[current_guess] == target:
#             return True
#         elif array[current_guess] < target:
#             current_min = current_guess + 1
#         else:
#             current_max = current_guess - 1
#         current_guess = (current_min + current_max) // 2
#
#     return False

# 개선답안_2
# def is_available_to_order(menus, orders):
#     menus_set = set(menus) #중복되지 않는 것만 추려내려면 set() 을 사용하면 됨(집합 자료형)
#     for order in orders:
#         if order not in menus_set:
#             return False
#     return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)