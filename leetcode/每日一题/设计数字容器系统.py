"""
设计一个数字容器系统，可以实现以下功能：

在系统中给定下标处 插入 或者 替换 一个数字。
返回 系统中给定数字的最小下标。

由于索引不确定 使用hash-map存储索引和值
但查找最小索引时 如果翻转列表浪费时间 可添加堆 记录数字对应索引 对于发生改变的位置需多次判断 直到索引位置为目标即可
"""

import heapq

class NumberContainers:

    def __init__(self):
        self.nums={}
        self.heap={}

    def change(self, index: int, number: int) -> None:
        self.nums[index]=number
        if number not in self.heap:
            self.heap[number]=[]
        heapq.heappush(self.heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.heap:
            return -1
        heap=self.heap[number]
        while heap and heap[0]!=number:
            heapq.heappop()
        return heap[0] if heap else -1
    
    