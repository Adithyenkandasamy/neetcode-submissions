class Solution:
    def trap(self, height: List[int]):
        # Edge Case
        if not height: return 0
        # Intialization
        res = 0
        l,r = 0,len(height)-1
        maxl,maxr = height[l],height[r]

        while l<r:# used for if the l is greater then r then it will stop like the limit end
            if maxl<maxr:
                l+=1
                maxl = max(height[l],maxl)
                res+=maxl-height[l]
            else:
                r-=1
                maxr = max(height[r],maxr)
                res+=maxr-height[r]
        return res        
