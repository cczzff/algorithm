# coding=utf-8
# 1.编写两个 Python 函数来寻找一个列表中的最小值。函数一将列表中的每个数都与其他数作比 较，数量级是 O(n²).函数二的数量级是 O(n)。


list_a = [3, 5, 8, 9, 4, 6]


def func1(items):
    for x in items:
        is_mix_value = True
        for y in items:
            if x > y:
                is_mix_value = False

        if is_mix_value:
            return x


def func2(items):
    mix_value = items[0]
    for item in items:
        if item < mix_value:
            mix_value = item
    return mix_value


if __name__ == '__main__':
    print func1(list_a)
    print func2(list_a)
