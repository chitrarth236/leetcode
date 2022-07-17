class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        p = []
        res = []
        self.helper(p,candidates, target,res)
        return res
    
    def helper(self, p, up, target,res):
        
        if target == 0:
            res.append(p)
            return
            
        if target < 0:
            return
        
        if len(up) == 0:
            return
        
        c = p.copy()
        c.append(up[0])
        
        self.helper(c, up, target - up[0],res)
        
        self.helper(p, up[1:], target,res)
        