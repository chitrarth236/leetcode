class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(nums) - 1
        result = [0,0]
        
        
        while(start <= end):
            mid = start + (end - start)//2
            
            if nums[mid] == target:
                first = mid
                last = mid
                
                while(first > -1 and nums[first] == target):
                    first-=1
                    
                while(last < len(nums) and nums[last] == target):
                    last+=1
                
                return [first + 1,last - 1]
            
            if nums[mid] < target:
                start = mid + 1
                
            if nums[mid] > target:
                end = mid - 1
                
        return [-1, -1]
        