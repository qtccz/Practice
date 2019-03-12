#!/usr/bin/python
# -*- coding:utf-8 -*-

result = list()

"""
    斐波那契数列的定义
    f(0) = 1
    f(1) = 1
    f(n) = f(n-1) + f(n-2)
"""


# 1、斐波那契 递归(recursive)
def fibonacci_recursive(number):
    if isinstance(number, int):
        if number < 0:
            raise RecursionError("error number")
        if 0 <= number <= 1:
            return number
        else:
            return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


def print_fibonacci_recursive(number):
    for n in range(1, number + 1):
        result.append(fibonacci_recursive(n))
    return result


# 斐波那契 循环(loop)
def fibonacci_loop(number):
    a, b = 0, 1
    while number > 0:
        result.append(b)
        a, b = b, a + b
        number -= 1
    return result


# 斐波那契 生成器(generator) 使用yield
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def print_fibonacci_generator():
    import itertools
    print("生成器实现: {}".format(list(itertools.islice(fibonacci_generator(), 0, 10))))


# 斐波那契 迭代器(iterator)
class Fib(object):

    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


def print_iterator_fibonacci():
    import itertools
    f = Fib()
    print("迭代器实现: {}".format(list(itertools.islice(f, 0, 5))))


def main():
    print_fibonacci_generator()
    print_iterator_fibonacci()


if __name__ == '__main__':
    main()
