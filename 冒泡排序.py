# coding=utf-8
# 冒泡排序

list_a = [1, 3, 2, 6, 19, 22, 33, 21, 4]


def bubble_sort(items):
    count = len(items)
    for x in range(1, count + 1):
        for y in range(len(items) - x):
            if items[y] > items[y+1]:
                items[y], items[y+1] = items[y+1], items[y]

    return items


if __name__ == '__main__':
    print bubble_sort(list_a)
