class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        processed = []
        self.helper(processed,nums, result)
        return result
        
    def helper(self, p, up, result):
        if len(up) == 0:
            result.append(p)
            return
        cp = p.copy()
        cp.append(up[0])
        self.helper(cp, up[1:], result)
        self.helper(p, up[1:], result)