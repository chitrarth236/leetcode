class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        N = len(nums)
        
        while(i < N):
            if(nums[i] != nums[nums[i] - 1]):
                nums[nums[i] - 1], nums[i]  =  nums[i], nums[nums[i] - 1]
            else:
                i+= 1
                
        for idx, i in enumerate(nums):
            if idx != i - 1:
                return i
        