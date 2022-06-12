class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the pivot element index first
        pivot = self.findPivot(nums)
        print(pivot)
        if(pivot == -1):
            return self.BinarySearch(nums, target, 0, len(nums) - 1)
        else:
            elem = self.BinarySearch(nums, target, 0, pivot)
            if(elem != -1):
                return elem
        return self.BinarySearch(nums, target, pivot + 1, len(nums) - 1)
            
        
        
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
    
    def BinarySearch(self, nums, target, start, end):
        while(start <= end):
            mid = start + (end - start) // 2
            
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1