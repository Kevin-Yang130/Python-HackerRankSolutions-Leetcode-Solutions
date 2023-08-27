# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #BFS approach
        if not root:
            return 0
        
        queue=[root]
        level=1
        while queue:
            level_length=len(queue)
            for i in range(level_length):
                temp=queue.pop(0)
                if  temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                if not temp.right and not temp.left:
                    return level
            level+=1
        return level

        # queue=[9,20]
        # level=1
        
        
