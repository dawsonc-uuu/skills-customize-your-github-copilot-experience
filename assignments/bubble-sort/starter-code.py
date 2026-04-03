#!/usr/bin/env python3
"""
Starter code for Bubble Sort assignment.
示例实现包含基本功能和简单测试；学生可修改或替换实现以完成作业。
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """示例实现：返回升序排序的新列表（不修改原始列表）。"""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def main() -> None:
    tests = [
        [5, 3, 8, 1, 2],
        [],
        [1, 2, 3, 4],
        [3, 3, 1, 2]
    ]

    for t in tests:
        print("Before:", t)
        print("After :", bubble_sort(t))
        print("---")


if __name__ == '__main__':
    main()
