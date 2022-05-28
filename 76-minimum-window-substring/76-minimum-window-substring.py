class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        nS = len(s)
        nT = len(t)
        i = 0
        res = float("infinity")
        
        
        Map = {}
        for ch in t:
            if ch not in Map:
                Map[ch] = 1
            else:
                Map[ch] += 1
        
        Need = len(Map)
        Have = 0
        W = {}
        rl = []
        
        if nS < nT:
            return ""
            
        for j in range(nS):
            W[s[j]] = 1 + W.get(s[j],0)
            
            if s[j] in Map and W[s[j]] == Map[s[j]]:
                Have += 1
            
            while(Need == Have):    
                if res > j - i + 1:
                    res = j - i + 1
                    rl = [i,j]
                W[s[i]] -= 1
                if s[i] in Map and W[s[i]] < Map[s[i]]:
                    Have-=1
                i+=1
        
        return s[rl[0]:rl[1] + 1] if res != float("infinity") else ""
        