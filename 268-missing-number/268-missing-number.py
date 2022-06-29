class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        N = len(nums)
        
        while(i < N):
            if(nums[i] < N and nums[i] != nums[nums[i]]):
                nums[nums[i]], nums[i]  =  nums[i], nums[nums[i]]
            else:
                i+= 1
                
        for idx, i in enumerate(nums):
            if idx != i:
                return idx
        return N
        