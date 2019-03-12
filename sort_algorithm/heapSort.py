#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
6、堆排序

堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，
它是选择排序的一种。可以利用数组的特点快速定位指定索引的元素。
堆分为大根堆和小根堆，是完全二叉树。
大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。
在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。

"""


# 指定列表下标元素交换位置并返回交换位置后列表
def swap_param(lists, i, j):
    lists[i], lists[j] = lists[j], lists[i]
    return lists


def heap_adjust(lists, start, end):
    temp = lists[start]
    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (lists[j] < lists[j + 1]):
            j += 1
        if temp < lists[j]:
            lists[i] = lists[j]
            i = j
            j = 2 * i
        else:
            break
    lists[i] = temp


def heap_sort(lists):
    lists_length = len(lists) - 1

    first_sort_count = lists_length // 2
    for i in range(first_sort_count):
        heap_adjust(lists, first_sort_count - i, lists_length)

    for i in range(lists_length - 1):
        lists = swap_param(lists, 1, lists_length - i)
        heap_adjust(lists, 1, lists_length - i - 1)

    return [lists[i] for i in range(1, len(lists))]


def main():
    from collections import deque
    import numpy as np
    lists = deque(np.random.randint(1, 100, size=10))
    lists.appendleft(0)
    print("堆排序前", lists)
    print("堆排序后", heap_sort(lists))


if __name__ == '__main__':
    main()
