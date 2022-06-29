class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        N = len(nums)
        
        while(i < N):
            if(nums[i] != nums[nums[i] - 1]):
                nums[nums[i] - 1], nums[i]  =  nums[i], nums[nums[i] - 1]
            else:
                i+= 1
        missing_nums = []       
        for idx, i in enumerate(nums):
            if idx != i - 1:
                missing_nums.append(i)
        return missing_nums
        