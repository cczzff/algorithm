# coding=utf-8
# 选择排序

list_a = [1, 3, 2, 6, 19, 22, 33, 5, 4]


def select_sort(items):

    for x in range(len(items)):
        max = items[0]
        max_index = 0
        for i in range(len(items) - x):
            if items[i] > max:
                max = items[i]
                max_index = i
        need_wait_index = -1-x
        items[need_wait_index], items[max_index] = items[max_index], items[need_wait_index]

    return items


if __name__ == '__main__':
    print select_sort(list_a)
