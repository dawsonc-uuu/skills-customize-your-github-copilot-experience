# 📘 Assignment: 冒泡算法（Bubble Sort）

## 🎯 Objective

实现并理解冒泡排序算法（Bubble Sort），练习数组/列表操作、循环与比较交换逻辑，并能分析算法的时间复杂度和优化方法。

## 📝 Tasks

### 🛠️ 主要任务：实现冒泡排序函数

#### Description

编写一个 `bubble_sort` 函数，接收整数列表并返回排序后的新列表（升序）。编写命令行测试，接受用户输入或使用预定义测试用例来验证你的实现。

#### Requirements

Completed program should:

- 实现 `bubble_sort(arr: list[int]) -> list[int]` 函数，返回已排序的列表
- 不使用内置排序函数（如 `list.sort()` 或 `sorted()`）来完成排序
- 在主程序或测试函数中展示若干测试用例（包括重复元素、空列表和已排序列表）
- 输出排序前后的列表以便验证

### 🛠️ 可选扩展任务：优化与分析

#### Description

在实现基础功能后，可完成以下可选项以加深理解。

#### Requirements

- 添加“提前退出”优化：检测一轮中是否发生交换，从而在数组已排序时提前结束循环
- 记录并输出比较与交换的次数，用以分析性能
- （可选）实现降序排序或基于用户选择的多种排序模式
- （可选）为算法绘制简单的步骤日志或可视化输出


---

示例运行方式（在包含 `starter-code.py` 的目录中运行）：

```bash
python3 starter-code.py
```
