class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
            return self.atmostK(nums,k)-self.atmostK(nums,k-1)

    def atmostK(self,nums,k):
        cnt=0
        i=0
        j=0
        d = dict()
        while i<len(nums):
            d[nums[i]] = d.get(nums[i],0) + 1
            while len(d)>k:
                d[nums[j]] -= 1
                if d[nums[j]] == 0:
                    d.pop(nums[j])
                j+=1
            cnt += i-j+1
            i+=1
        return cnt