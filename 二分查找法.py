# coding=utf-8

list_a = [1, 3, 5, 6, 8, 9, 13, 14, 15, 18]


def binary_search(target, items):
    mid = len(items) // 2
    mid_item = items[mid]
    if target == mid_item:
        return True

    if len(items) == 1:
        return False

    if target > mid_item:
        return binary_search(target, items[mid:])

    if target < mid_item:
        return binary_search(target, items[:mid])


if __name__ == '__main__':
    print binary_search(22, list_a)
