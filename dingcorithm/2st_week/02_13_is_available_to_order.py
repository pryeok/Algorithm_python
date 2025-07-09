shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


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


result = is_available_to_order(shop_menus, shop_orders)
print(result)