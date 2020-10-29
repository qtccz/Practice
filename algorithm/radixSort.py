#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
8、基数排序（radix sort）
基数排序属于“分配式排序”（distribution sort），
又称“桶子法”（bucket sort）或bin sort，顾名思义，
它是透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用，
基数排序法是属于稳定性的排序，其时间复杂度为O (nlog(r)m)，其中r为所采取的基数，
而m为堆数，在某些时候，基数排序法的效率高于其它的稳定性排序法。

排序过程:
首先将所有待比较数值统一为统一位数长度，接着从最低位开始，依次进行排序。
1. 按照个位数进行排序。
2. 按照十位数进行排序。
3. 按照百位数进行排序。
排序后，数列就变成了一个有序序列。

"""

import math


def radix_sort(lists, radix=10):
    # 获取列表中最大值得位数
    k = int(math.ceil(math.log(max(lists), radix)))
    # 生成radix个空列表
    bucket = [[] for _ in range(radix)]
    # 获取数值位数
    for i in range(1, k + 1):
        for j in lists:
            # 按照数值的位数大小放入对应的bucket中
            bucket[j // (radix ** (i - 1)) % (radix ** i)].append(j)
        # 清除lists全部元素
        del lists[:]
        for z in bucket:
            # 将bucket中的元素追加进lists中
            lists += z
            # 清除z中元素
            del z[:]
    return lists


def main():
    import numpy as np
    lists = list(np.random.randint(0, 100, size=10))
    print("排序前", lists)
    print("排序后", radix_sort(lists))


if __name__ == '__main__':
    main()

