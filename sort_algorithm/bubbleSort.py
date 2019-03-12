#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
3、冒泡排序

它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

步骤：
1、比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3、针对所有的元素重复以上的步骤，除了最后一个。
4、持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""


def bubble_sort(lists):
    count = len(lists)
    for i in range(count - 1, 0, -1):  # range(count - 1, 0, -1) 表示每次便利需要比较的次数，逐渐减小的
        for j in range(i):
            if lists[i] < lists[j]:  # i表示列表最后一位, j表示列表中的每一位
                lists[i], lists[j] = lists[j], lists[i]
    return lists


def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(bubble_sort(alist))


if __name__ == '__main__':
    main()
