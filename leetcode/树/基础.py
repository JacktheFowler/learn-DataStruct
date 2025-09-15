from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


# 树为非线性数据结构 满二叉树 完全二叉树 完满二叉树「所有节点均有连个子节点 平衡二叉树 所有节点高度差距<=1

# BFS
# 先序遍历
res=[]
def preOrder(root:TreeNode|None=None):
    if root is None:
        return
    res.append(root.val)
    preOrder(root.left)
    preOrder(root.right)

def level_order(root: TreeNode | None = None):
    queue = deque([root])
    res = []
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res

# 搜索树 本质上二分查找 中间结点为根 left<root<right
# 使用中序遍历 可得到升序数组
class BinarySearchTree(TreeNode):
    def search(self, num):
        cur=self._root
        while cur is not None:
            if cur.val>num:
                cur=cur.left
            elif cur.val<num:
                cur=cur.right
            else:
                break
        return cur
    # 若在插入时找到返回 None
    def insert(self, num):
        if self._root is None:
            return
        cur, pre=self._root, None
        while cur is not None:
            if cur.val==num:
                return
            pre=cur
            if cur.val>num:
                cur=cur.left
            else:
                cur=cur.right
        if pre.val>num:
            return pre.left
        else:
            return pre.right
    
    # 删除子节点
    def remove(self, num):
        if self._root is None:
            return
        cur, pre=self._root, None
        while cur is not None:
            pre=cur
            if cur.val>num:
                cur=cur.left
            elif cur.val<num:
                cur=cur.right
            else:
                break

        if cur is None:
            return
        # 只有1个子节点 可用子节点替代
        if cur.left is None or cur.right is None:
            child=cur.left or cur.right
            if cur!=self.root:
                if pre.left==cur:
                    pre.left=child
                else:
                    pre.right=child
            else:
                self._root=child
        # 有2个子节点 用最靠近中间的节点替换 即右子树最左的节点
        else:
            tmp=cur.right
            while tmp.left is not None:
                tmp=tmp.left
            # 递归删除
            self.remove(tmp.val)
            cur.val=tmp.val

if __name__ == "__main__":
    tree = [TreeNode(i) for i in range(1, 8)]
    root = tree[0]
    root.left = tree[1]
    root.right = tree[2]
    tree[1].left = tree[3]
    tree[1].right = tree[4]
    tree[2].left=tree[5]
    tree[2].right=tree[6]

    # print(level_order(root))
    preOrder(root)
    print(res)
