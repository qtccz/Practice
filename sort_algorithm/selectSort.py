#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
5、直接选择排序

基本思想：
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。

"""


def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        # 假设找到的最小元素下标为i
        min_index = i
        # 寻找最小元素的过程
        for j in range(i + 1, count):
            # 假设最小下标的值，大于循环中一个元素，那么就改变最小值的下标
            if lists[min_index] > lists[j]:
                min_index = j
        # 在不停的循环中，不停的交换两个不一样大小的值
        lists[min_index], lists[i] = lists[i], lists[min_index]
    return lists


def main():
    import numpy as np
    arr = np.random.randint(0, 100, size=10)
    print(select_sort(arr))


if __name__ == '__main__':
    main()
