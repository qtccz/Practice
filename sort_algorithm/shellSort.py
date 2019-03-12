#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
2、希尔排序

希尔排序(Shell Sort)是插入排序的一种。
也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。
希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，
整个文件恰被分成一组，算法便终止。
"""


def shell_sort(lists):
    count = len(lists)
    group = count // 2
    while group >= 1:
        for j in range(group, count):
            i = j
            while (i - group) >= 0:
                if lists[(i - group)] > lists[i]:
                    lists[i], lists[(i - group)] = lists[(i - group)], lists[i]
                    i -= group
                else:
                    break
        group //= 2
    return lists


def main():
    alist = [8, 6, 4, 9, 7, 3, 2, -4, 0, -100, 99]
    print(shell_sort(alist))


if __name__ == '__main__':
    main()
