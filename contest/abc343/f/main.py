import sys
def I():
    return int(sys.stdin.readline())
def MI():
    return map(int, sys.stdin.readline().split())
def LI():
    return list(map(int, sys.stdin.readline().split()))


class Node:
    def __init__(self):
        self.max_val = -1
        self.second_max_val = -1
        self.second_max_count = 0

def merge(left, right):
    node = Node()
    values = sorted([left.max_val, right.max_val, left.second_max_val, right.second_max_val], reverse=True)
    node.max_val = values[0]
    unique_values = list(set(values))
    if len(unique_values) > 1:
        node.second_max_val = unique_values[1]
    if node.second_max_val != -1:
        if left.second_max_val == node.second_max_val:
            node.second_max_count += left.second_max_count
        if right.second_max_val == node.second_max_val:
            node.second_max_count += right.second_max_count
        if left.max_val == node.second_max_val:
            node.second_max_count += 1
        if right.max_val == node.second_max_val:
            node.second_max_count += 1
    return node

class SegmentTree:
    def __init__(self, A):
        self.size = len(A)
        self.tree = [Node() for _ in range(4 * self.size)]
        self.build(A)

    def build(self, A, node=1, l=0, r=None):
        if r is None:
            r = self.size - 1
        if l == r:
            self.tree[node].max_val = A[l]
            return
        mid = (l + r) // 2
        self.build(A, node * 2, l, mid)
        self.build(A, node * 2 + 1, mid + 1, r)
        self.tree[node] = merge(self.tree[node * 2], self.tree[node * 2 + 1])

    def update(self, idx, val, node=1, l=0, r=None):
        if r is None:
            r = self.size - 1
        if l == r:
            self.tree[node].max_val = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(idx, val, node * 2, l, mid)
        else:
            self.update(idx, val, node * 2 + 1, mid + 1, r)
        self.tree[node] = merge(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, start, end, node=1, l=0, r=None):
        if r is None:
            r = self.size - 1
        if start > r or end < l:
            return Node()
        if start <= l and r <= end:
            return self.tree[node]
        mid = (l + r) // 2
        left = self.query(start, end, node * 2, l, mid)
        right = self.query(start, end, node * 2 + 1, mid + 1, r)
        return merge(left, right)

N,Q=MI()
A=LI()

seg_tree = SegmentTree(A)

for i in range(Q):
    q = LI()
    if q[0] == 1:
        p, x = q[1], q[2]
        seg_tree.update(p - 1, x)
    
    if q[0] == 2:
        l, r = q[1], q[2]
        result = seg_tree.query(l - 1, r - 1)
        if i != 0 and i == Q - 1:
            print(result.second_max_count + 1)
        else:
            print(result.second_max_count)

