# https://leetcode.com/problems/array-nesting/

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        maxcounter=0
        tempmax=0
        temp=0
        
        for i in nums:           
            while nums[i]>=0:         
                tempmax += 1
                
                temp=nums[i]
                nums[i]=-1
                i=temp
        
            maxcounter = max(maxcounter,tempmax)
            tempmax = 0

        return maxcounter