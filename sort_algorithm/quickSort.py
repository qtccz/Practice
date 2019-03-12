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
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        # print('right', array)
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
        # print('left', array)
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)
    return array


def main():
    import numpy as np
    alists = np.random.randint(0, 100, size=10)
    print(quick_sort(alists, 0, np.size(alists) - 1))

    # sorted_arr = np.sort(alists)
    # quick_sort(alists, 0, np.size(alists) - 1)
    # assert (sorted_arr.all() == alists.all())


if __name__ == '__main__':
    main()
