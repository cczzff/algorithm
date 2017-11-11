# coding=utf-8
# 快速排序

list_a = [3, 2, 4, 8, 5, 1, 7]


def quick_sort(items):
    if not items:
        return []

    key = items[0]
    left = []
    right = []

    for i in range(len(items)):
        if key > items[i]:
            left.append(items[i])
        elif key < items[i]:
            right.append(items[i])

    left = quick_sort(left)
    right = quick_sort(right)
    return left + [key] + right


if __name__ == '__main__':
    print quick_sort(list_a)