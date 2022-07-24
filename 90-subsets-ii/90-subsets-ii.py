class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        processed = []
        nums.sort()
        self.helper(processed,nums, 0, result,True)
        return result
        
    def helper(self, p, up, i, result, isPicked):
        if i >= len(up):
            result.append(p)
            return
        cp = p.copy()
        cp.append(up[i])
        
        if i == 0 or up[i] != up[i - 1] or isPicked:
            #i = i + 1
            self.helper(cp, up, i+1, result,True)
        self.helper(p, up, i+1, result, False)