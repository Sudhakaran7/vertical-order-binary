from binarytree import build 
import collections


# BFS + hash solution.
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in range(min(cols.keys()),
                                        max(cols.keys()) + 1)] if cols else []

n=int(input())
nodes =list(map(int,input().split())) 
binary_tree = build(nodes) 
val=Solution()
print(*val.verticalOrder(binary_tree))
