class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        pivot = self.findPivot(nums)
        
        return nums[(pivot + 1) % len(nums)]
        
        
        """start = 0
        end = len(nums) - 1
        N = len(nums)
        res = nums[start]
        while(start <= end):
            
            if nums[start] < nums[end]:
                return nums[start]
            
            mid = start + (end - start)//2
            
            if(nums[mid] < nums[(mid + 1)%N] and nums[mid] < nums[(mid - N + 1)%N]):
                return nums[mid]
            else:
                if nums[start] < nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return res""" 
    
    def findPivot(self, nums):
        start, end = 0, len(nums) - 1
        
        
        
        while(start <= end):
            mid = start + (end - start) // 2
            
            if mid < end and nums[mid] > nums[mid + 1]:
                return mid
            
            if mid > start and nums[mid] < nums[mid - 1]:
                return mid - 1
            
            if nums[mid] <= nums[start]:
                end = mid - 1
            else:
                start = mid + 1      
        return -1
        