# https://leetcode.com/contest/biweekly-contest-60/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        #print(nums)
        if len(nums) == 1:
            return 0
        
        left = 0
        right = sum(nums)
        right -= nums[0]

        if left==right:
            return 0

        for i in range(1,len(nums)):
            left += nums[i-1]
            right -= nums[i]

            #print(i,left,right)
            if left == right:
                return i
        return -1

aa =Solution()
zz= [3,-3,4]
ans = aa.findMiddleIndex(zz)
print(ans)