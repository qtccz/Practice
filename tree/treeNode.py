#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
创建一个树的类，并给一个root根节点，一开始为空，随后添加节点;

"""


class Node(object):
    """二叉树节点"""
    def __init__(self):
        self.elem = -1
        self.leftChild = None
        self.rightChild = None

