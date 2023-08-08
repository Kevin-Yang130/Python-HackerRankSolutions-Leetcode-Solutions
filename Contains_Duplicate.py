class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = 0
        for i in range(len(nums)):
            d[nums[i]] +=1
        for num, freq in d.items():
            if (freq > 1):
                return True
        return False
