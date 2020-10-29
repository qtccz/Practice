#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
4、快速排序

通过一趟排序将要排序的数据分割成独立的两部分，
其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，
整个排序过程可以递归进行，以此达到整个数据变成有序序列。

快速排序图文详解: http://www.cnblogs.com/ahalei/p/3568434.html

"""


def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]  # 基准数
    while left < right:
        # 如果右侧的数值大于key，下标前移一位
        while left < right and array[right] > key:
            right -= 1
        # 数值小的替换到左边
        array[left] = array[right]
        # 如果左侧的数值小于等于key，下标后移一位
        while left < right and array[left] <= key:
            left += 1
        # 数值大的替换到右边
        array[right] = array[left]
    array[right] = key  # 基准数归位
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)
    return array


def main():
    import numpy as np
    alist = list(np.random.randint(0, 100, size=10))
    print("排序前", alist)
    print("排序后", quick_sort(alist, 0, np.size(alist) - 1))


if __name__ == '__main__':
    main()

