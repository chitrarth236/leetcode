class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.helper(num,0)
        
    def helper(self, num, count):
        if num == 0:
            return count
        
        if num%2 == 0:
            return self.helper(num//2,count+1)
        else:
            return self.helper(num - 1, count + 1)