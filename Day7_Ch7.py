# Binary Tree
from modules import TreeNode
from collections import deque
# Breadth-First Search(BFS)
def level_order(root: TreeNode | None) -> list[int]:
    queue: deque[TreeNode] = deque()
    queue.append(root)
    res = []
    while queue:
        node: TreeNode = queue.popleft()
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res

# Depth-First Search(DFS)
def pre_order(root: TreeNode | None):
    if root is None:
        return
    # Root -> Left Subtree -> Right Subtree
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)

def in_order(root: TreeNode | None):
    if root is None:
        return
    # Left Subtree -> Root -> Right Subtree
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)

def post_order(root: TreeNode | None):
    if root is None:
        return
    # Left Subtree -> Right Subtree -> Root
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)

# Array_Binary_Tree
class ArrayBinaryTree:
    def __init__(self, arr: list[int | None]):
        self._tree = list(arr)

    def size(self):
        return len(self._tree)
    
    def val(self, i: int) -> int | None:
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]

    def left(self, i: int) -> int | None:
        return 2 * i + 1
    
    def right(self, i: int) -> int | None:
        return 2 * i + 2
    
    def parent(self, i: int) -> int | None:
        return (i - 1) // 2
    
    def level_order(self) -> list[int]:
        self.res = []
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res
    
    def dfs(self, i: int, order: str):
        if self.val(i) is None:
            return
        if order == "pre":
            self.res.append(self.val(i))
        self.dfs(self.left(i), order)
        if order == "in":
            self.res.append(self.val(i))
        self.dfs(self.right(i), order)
        if order == "post":
            self.res.append(self.val(i))

    def pre_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order="pre")
        return self.res
    
    def in_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order="in")
        return self.res
    
    def post_order(self) -> list[int]:
        self.res = []
        self.dfs(0, order="post")
        return self.res

# Binary Search Tree
def search(self, num: int) -> TreeNode | None:
    cur = self._root
    while cur is not None:
        if cur.val < num:
            cur = cur.right
        elif cur.val > num:
            cur = cur.left
        else:
            break
    return cur

def insert(self, num: int):
    if self._root is None:
        self._root = TreeNode(num)
        return
    cur, pre = self._root, None
    while cur is not None:
        if cur.val == num:
            return
        pre = cur
        if cur.val < num:
            cur = cur.right
        else:
            cur = cur.left
    node = TreeNode(num)
    if pre.val < num:
        pre.right = node
    else:
        pre.left = node

def remove(self, num: int):
    if self._root is None:
        return
    cur, pre = self._root, None
    while cur is not None:
        if cur.val == num:
            break
        pre = cur
        if cur.val < num:
            cur = cur.right
        else:
            cur = cur.left
    if cur is None:
        return
    if cur.left is None or cur.right is None:
        child = cur.left or cur.right
        if cur != self._root:
            if pre.left == cur:
                pre.left = child
            else:
                pre.right = child
        else:
            self._root = child
    else:
        tmp: TreeNode = cur.right
        while tmp.left is not None:
            tmp = tmp.left
            self.remove(tmp.val)
            cur.val = tmp.val

# AVL Tree
def height(self, node: TreeNode | None) -> int:
    if node is not None:
        return node.height
    return -1

def update_height(self, node: TreeNode | None):
    node.height = max([self.height(node.left), self.height(node.right)]) + 1

def balance_factor(self, node: TreeNode | None) -> int:
    if node is None:
        return 0
    return self.height(node.left) - self.height(node.right)

def right_rotate(self, node: TreeNode | None) -> TreeNode | None:
    child = node.left
    grand_child = child.right
    child.right = node
    node.left = grand_child
    self.update_height(node)
    self.update_height(child)
    return child

def left_rotate(self, node: TreeNode | None) -> TreeNode | None:
    child = node.right
    grand_child = child.left
    child.left = node
    node.right = grand_child
    self.update_height(node)
    self.update_height(child)
    return child

def rotate(self, node: TreeNode | None) -> TreeNode | None:
    balance_factor = self.balance_factor(node)
    # Left Side Tree
    if balance_factor > 1:
        if self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)
        else:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
    # Right Side Tree
    elif balance_factor < -1:
        if self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)
        else:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
    return node

def insert(self, val):
    self._root = self.insert_helper(self._root, val)

def insert_helper(self, node: TreeNode | None, val: int) -> TreeNode:
    if node is None:
        return TreeNode(val)
    if val < node.val:
        node.left = self.insert_helper(node.left, val)
    elif val > node.val:
        node.right = self.insert_helper(node.right, val)
    else:
        return node
    self.update_height(node)
    return self.rotate(node)

def remove(self, val: int):
    self._root = self.remove_helper(self._root, val)

def remove_helper(self, node: TreeNode | None, val: int) -> TreeNode | None:
    if node is None:
        return None
    if val < node.val:
        node.left = self.remove_helper(node.left, val)
    elif val > node.val:
        node.right = self.remove_helper(node.right, val)
    else:
        if node.left is None or node.right is None:
            child = node.left or node.right
            if child is None:
                return None
            else:
                node = child
        else:
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            node.right = self.remove_helper(node.right, temp.val)
            node.val = temp.val
    self.update_height(node)
    return self.rotate(node)


if __name__ == '__main___':
    res = []
