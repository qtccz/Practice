#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
3、冒泡排序

它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
时间复杂度达到了O(N²)

步骤：
1、比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3、除了最后一个元素外，针对所有的元素重复以上的步骤。
4、持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""


def bubble_sort(lists):
    count = len(lists)
    # range(count - 1, 0, -1) 从大到小依次得到待排序数值次数；次数是逐渐减小
    for lastIndex in range(count - 1, 0, -1):
        for j in range(lastIndex):
            # lastIndex表示列表最后一位, j表示列表中lastIndex之前的每一位
            if lists[lastIndex] < lists[j]:
                lists[lastIndex], lists[j] = lists[j], lists[lastIndex]
    return lists


def main():
    import numpy as np
    alist = list(np.random.randint(0, 100, size=10))
    print("排序前:", alist)
    print("排序后:", bubble_sort(alist))


if __name__ == '__main__':
    main()


