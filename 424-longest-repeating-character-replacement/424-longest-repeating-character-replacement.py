class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        
        i = 0
        L = 0
        Map = {}
        
        for j in range(len(s)):
            Map[s[j]] = 1 + Map.get(s[j],0)
            
            N = len(s[i:j+1]) - max(Map.values())
            
            while(N > k):
                Map[s[i]] -= 1
                
                if(Map[s[i]] == 0):
                    Map.pop(s[i])
                    
                i+= 1
                N = len(s[i:j+1]) - max(Map.values())
                    
            if N <= k:
                L = max(j - i + 1, L)
                
        return L
        