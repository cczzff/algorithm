# coding=utf-8
# 希尔排序


list_a = [3, 2, 4, 8, 5, 1, 7]


def shell_sort(items):
    count = len(items)
    step = 2
    while count / step >= 0:
        offset = 0
        while True:
            piece = items[offset * step: (offset + 1) * step]
            if not piece:
                break
            piece = select_sort(piece)
            items[offset * step: (offset + 1) * step] = piece
            offset += 1
        # 如果 count / step == 0 说明就这一组了
        if count / step == 0:
            break
        # 步伐变大
        step *= 2

    return items


def select_sort(items):
    # 插入排序
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
    print shell_sort(list_a)
