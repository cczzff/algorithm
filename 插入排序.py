# coding=utf-8
# 插入排序


list_a = [3, 2, 4, 8, 5, 1, 7]


def insert_sort(items):
    count = len(items)
    for i in range(count):
        key = items[i]
        key_index = i
        while i > 0:
            if items[i-1] > key:
                items[i-1], items[key_index] = items[key_index], items[i-1]
                key_index = key_index - 1

            i = i - 1

    return items


if __name__ == '__main__':
    print insert_sort(list_a)
