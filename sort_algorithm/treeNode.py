#!/usr/bin/python
# -*- coding:utf-8 -*-


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreePrinter(object):

    def __init__(self):
        pass

    def printTree(self, root):
        queue = []  # 定义一个队列，用来存放二叉树中的结点（原始）
        temp = []   # 定义一个临时列表，用来存放每一层遍历出的结点（临时）
        result = [] # 定义一个空列表，用来存放最终供打印输出的结点（最终）

        if root == None:
            return result
        last = nlast = root
        queue.append(root)

        while len(queue):
            node = queue.pop(0)

            temp.append(node.val)

            if node.left != None:
                queue.append(node.left)
                nlast = node.left

            if node.right != None:
                queue.append(node.right)
                nlast = node.right

            if node == last:
                result.append(temp[:])
                temp = []
                last = nlast
        return result
