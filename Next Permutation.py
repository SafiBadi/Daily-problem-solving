class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        if len(nums) == 1: # edge case. If len(nums) == 1 we can't find next permutation
            return

        for i in reversed(range(1, len(nums))):
            if nums[i] > nums[i-1]: 
                temp = min(m for m in nums[i:] if m>nums[i-1]) # find temp just greter than nums[i-1] from nums[i:]
                min_index = nums.index(temp,i) # find index of temp

                nums[i-1], nums[min_index]  = nums[min_index], nums[i-1] # swap temp and nums[i-1]

                nums[i:] = sorted(nums[i:]) # sort the remaining nums[i:] in ascending order for smallest next permutation
                return

        if i == 1:
            nums.sort() #If we can't fingd next permutation -> according to problem statment return smalles permutation.
            return



t = Solution()

nums = [2,3,1,3,3]


t.nextPermutation(nums)
print(nums)