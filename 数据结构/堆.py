import heapq

# 计算机系统内存中的堆是动态内存分配的一部分，程序在运行时可以使用它来存储数据
# 当数据不需要时 程序应释放空间 防止内存泄漏
class heap:
    def __init__(self, nums:list):
        self.max_heap = nums
        # 建堆两种方案 逐元素入堆 O(nlogn)
        # 倒序节点入堆 O(n)
        for i in range(self.parent(self.size()-1), -1, -1):
            self.sift_down(i)

    def size(self):
        return len(self.max_heap)
    
    def is_empty(self):
        return False if self.size() else True

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def peek(self):
        return self.max_heap[0]
    # 入堆
    def push(self, val):
        self.max_heap.append(val)
        self.sift_up(self.size()-1)

    def swap(self, i, j):
        self.max_heap[i], self.max_heap[j]=self.max_heap[j], self.max_heap[i]

    # 自底至顶堆化
    def sift_up(self, i):
        while True:
            p=self.parent(i)
            if p<0 or self.max_heap[i]<=self.max_heap[p]:
                break
            self.swap(i, p)
            i=p

    def pop(self):
        if self.is_empty():
            raise IndexError('堆为空')
        self.swap(0, self.size()-1)
        val=self.max_heap.pop()
        self.sift_down(0)
        return val
    
    def sift_down(self, i):
        while True:
            l, r, p=self.left(i), self.right(i), i
            if l<self.size() and self.max_heap[l]>self.max_heap[p]:
                p=l
            if r<self.size() and self.max_heap[r]>self.max_heap[p]:
                p=r
            if p==i:
                break
            self.swap(i, p)
            i=p

# top-k问题 维持k小顶堆 当num>heap[0] 入堆 时间复杂度为nlog(k)
def topk(nums:list, k):
    h=[]
    for i in range(k):
        heapq.heappush(h, nums[i])
    for i in range(k, len(nums)):
        if nums[i]>h[0]:
            heapq.heappop(h)
            heapq.heappush(h, nums[i])
    return h

if __name__ == "__main__":
    # 小顶堆与大顶堆的转化
    def TestMaxheap():
        max_heap, flag = [], -1
        heapq.heappush(max_heap, 1 * flag)
        heapq.heappush(max_heap, 2 * flag)
        heapq.heappush(max_heap, 3 * flag)
        heapq.heappush(max_heap, 4 * flag)
        heapq.heappush(max_heap, 5 * flag)

        # 出堆
        while max_heap:
            print(flag * heapq.heappop(max_heap))
    
    h=heap([2, 3, 7, 9, 4])
    print(h.pop())
