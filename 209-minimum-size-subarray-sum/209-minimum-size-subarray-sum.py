class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        Sum = 0
        i = 0
        
        mini = len(nums) + 1
        
        for j in range(len(nums)):
            
            Sum += nums[j]
            
            
            while(i <= j and Sum >= target):
                mini = min(mini, j-i+1)
                Sum -= nums[i]
                i+=1
                
                
            
                
        return mini if mini != len(nums)+1 else 0
                
        