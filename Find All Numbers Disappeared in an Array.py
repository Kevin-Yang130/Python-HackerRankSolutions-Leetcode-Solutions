class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    
        for n in nums:
            i  = abs(n) - 1  
            nums[i]= abs(nums[i]) * - 1
        re = []
        for i, n in enumerate(nums):
            if n > 0:
                re.append(i+1)
        return re
