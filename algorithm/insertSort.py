#!/usr/bin/python
# -*- coding:utf-8 -*-


"""
1、插入排序

基本操作就是将一个数据插入到已经排好序的有序数据中，
从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。

步骤：
1、将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列（即待插入元素）。
2、从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
    （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面）

"""


def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        preIndex = i - 1
        currentValue = lists[i]
        while preIndex >= 0:
            if lists[preIndex] > currentValue:
                lists[preIndex], lists[preIndex + 1] = currentValue, lists[preIndex]
            preIndex -= 1
    return lists


def main():
    import numpy as np
    alist = list(np.random.randint(-50, 50, size=10))
    print("排序前:", alist)
    print("排序后:", insert_sort(alist))


if __name__ == '__main__':
    main()

