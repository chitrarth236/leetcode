class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1,n+1)]
        processed = []
        result = []
        self.helper(processed,arr,k,result)
        return result
        
        
    def helper(self, p, up, k, result):
        if len(p) == k:
            result.append(p)
            return
        
        if len(up) == 0:
            return
        
        cp = p.copy()
        cp.append(up[0])
        self.helper(cp,up[1:],k,result)
        self.helper(p,up[1:],k,result)
            
        
        