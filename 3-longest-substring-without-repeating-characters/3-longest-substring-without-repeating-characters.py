class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        Map = {}
        i = 0 #Starting pointer
        maxi=0
        
        for j in range(len(s)):
            ch = s[j]
            
            if ch not in Map.keys():
                Map[ch] = 1
            else:
                Map[ch] += 1
                
            
            while(len(Map) < j - i + 1):
                f_ch = s[i]
                i+=1
                Map[f_ch] -= 1
                
                if Map[f_ch] == 0:
                    Map.pop(f_ch)
                
             
            if(j - i + 1 > maxi):
                maxi = j - i + 1
                
        return maxi
                