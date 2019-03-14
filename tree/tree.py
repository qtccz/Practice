#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
创建一个树的类，并给一个root根节点，一开始为空，随后添加节点;
"""


class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.leftChild = lchild
        self.rightChild = rchild


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.queue = []

    # 添加节点
    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.queue.append(self.root)
        else:
            treeNode = self.queue[0]
            if treeNode.leftChild is None:
                treeNode.leftChild = node
                self.queue.append(treeNode.leftChild)
            else:
                treeNode.rightChild = node
                self.queue.append(treeNode.rightChild)
                self.queue.pop(0)

    # 递归实现先序遍历
    def preOrder(self, root):
        if root is None:
            return
        print(root.elem, end="")
        self.preOrder(root.leftChild)
        self.preOrder(root.rightChild)

    # 递归实现中序遍历
    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.leftChild)
        print(root.elem, end="")
        self.inOrder(root.rightChild)

    # 递归实现后序遍历
    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.leftChild)
        self.postOrder(root.rightChild)
        print(root.elem, end="")

    # 深度遍历(队列)
    def depthOrder(self, root):
        if root is None:
            return
        queue = list()
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem, end="")
            if node.leftChild is not None:
                queue.append(node.leftChild)
            if node.rightChild is not None:
                queue.append(node.rightChild)
        print()

    # 堆栈实现树的先序遍历
    def preStackOrder(self, root):
        if root is None:
            return
        queue = list()
        node = root
        while queue or node:
            while node:                 # 从根节点开始，一直找它的左子树
                print(node.elem, end="")
                queue.append(node)
                node = node.leftChild
            node = queue.pop()          # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rightChild      # 开始查看它的右子树
        print()

    # 堆栈实现树的中序遍历
    def inStackOrder(self, root):
        if root is None:
            return
        queue = list()
        node = root
        while queue or node:
            while node:                 # 从根节点开始，一直找它的左子树
                queue.append(node)
                node = node.leftChild
            node = queue.pop()          # while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.elem, end="")
            node = node.rightChild      # 开始查看它的右子树
        print()

    # 堆栈实现树的后序遍历
    def postStackOrder(self, root):
        if root is None:
            return
        queue1 = list()
        queue2 = list()
        node = root
        queue1.append(node)
        while queue1:                           # while循环是找出后序遍历的逆序，存在queue2里面
            node = queue1.pop()
            if node.leftChild:
                queue1.append(node.leftChild)
            if node.rightChild:
                queue1.append(node.rightChild)
            queue2.append(node)
        while queue2:                           # 将queue2中的元素出栈，即为后序遍历次序
            print(queue2.pop().elem, end="")


def main():
    elems = range(10)
    tree = Tree()
    for elem in elems:
        tree.add(elem)


    print("递归实现先序遍历", end="\t")
    tree.preOrder(tree.root)
    print()
    print("递归实现中序遍历", end="\t")
    tree.inOrder(tree.root)
    print()
    print("递归实现后序遍历", end="\t")
    tree.postOrder(tree.root)
    print()
    print("深度遍历", end="\t")
    tree.depthOrder(tree.root)
    print("堆栈实现树的先序遍历", end="\t")
    tree.preStackOrder(tree.root)
    print("堆栈实现树的中序遍历", end="\t")
    tree.inStackOrder(tree.root)
    print("堆栈实现树的后序遍历", end="\t")
    tree.postStackOrder(tree.root)


if __name__ == '__main__':
    main()
