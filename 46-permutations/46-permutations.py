class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        proccessed = []
        result = []
        level = 1
        self.helper(proccessed, nums, level, result)
        return result
        
        
    def helper(self, p, up, level, result):
        
        if len(up) == 0:
            result.append(p)
            return
        
        new_p = []
        for i in range(level):
            new_p = p[0:i] + [up[0]] + p[i:]
            self.helper(new_p, up[1:], level + 1, result)