# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue, ans = [root], []
        while(queue):
            qsize = len(queue)
            rowSum = 0
            for i in range(qsize):
                temp = queue.pop(0)
                rowSum += temp.val
                if(temp.left):
                    queue.append(temp.left)
                if(temp.right):
                    queue.append(temp.right)
            ans.append(rowSum/qsize)
        return ans

        
